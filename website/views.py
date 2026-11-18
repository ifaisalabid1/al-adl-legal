from django.views.generic import TemplateView, DetailView, FormView, ListView
from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView
from django.db.models import Q

from blog.models import BlogModel
from .serializers import ServiceSerializer
from .forms import EnquiryForm, SearchForm
from .models import ServiceModel, TeamModel, FAQModel


class HomePageView(TemplateView):
    template_name = "website/pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = EnquiryForm
        context["services"] = ServiceModel.active.all()[:8]
        context["blogs"] = BlogModel.active.filter(featured=True)[:3]
        return context


class AboutUsView(TemplateView):
    template_name = "website/pages/about_us.html"


class TrademarkRegistrationView(TemplateView):
    template_name = "website/pages/trademark_registration.html"


class ContactUsView(TemplateView):
    template_name = "website/pages/contact_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = EnquiryForm
        return context


class ServicesView(ListView):
    template_name = "website/pages/services.html"
    queryset = ServiceModel.active.all().order_by("title")
    context_object_name = "services"
    paginate_by = 20


class FAQView(ListView):
    template_name = "website/pages/faq.html"
    queryset = FAQModel.active.all()
    context_object_name = "faqs"
    paginate_by = 20


class LegalTeamView(ListView):
    queryset = TeamModel.active.all()
    template_name = "website/pages/legal_team.html"
    context_object_name = "team"
    paginate_by = 20


class TeamMemberView(DetailView):
    queryset = TeamModel.active.all()
    template_name = "website/pages/member.html"
    context_object_name = "member"


class ServiceView(DetailView):
    queryset = ServiceModel.active.all()
    template_name = "website/pages/service.html"
    context_object_name = "service"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = EnquiryForm(
            initial={
                "service": self.get_object(),
            }
        )
        # Hide Enquiry and Service Widgets
        field = form.fields["service"]
        field.widget = field.hidden_widget()

        # Hide Enquiry and Service Widgets
        field = form.fields["type_of_query"]
        field.widget = field.hidden_widget()

        context["form"] = form
        return context


class EnquiryFormView(FormView):

    template_name = "website/includes/enquiry_form.html"
    form_class = EnquiryForm
    success_url = reverse_lazy("enquiry_form_thanks")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SearchView(TemplateView):

    template_name = "website/pages/search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data["q"]
            context["query"] = query
            context["services"] = ServiceModel.objects.filter(
                Q(name__icontains=query)
                | Q(title__icontains=query)
                | Q(body__icontains=query)
            )
            context["blogs"] = BlogModel.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
            context["faqs"] = FAQModel.objects.filter(
                Q(question__icontains=query) | Q(answer__icontains=query)
            )
        else:
            context["error"] = True

        return context


class ServicesAPIView(ListAPIView):
    queryset = ServiceModel.objects.all()
    # authentication_classes = []
    serializer_class = ServiceSerializer
