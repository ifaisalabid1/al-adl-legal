from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, TemplateView, FormView,
)
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import *
from .forms import *

from formtools.wizard.views import SessionWizardView


class HomePageView(TemplateView):
    template_name = "develawp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context['courses'] = CourseModel.active.filter(
            date__gte=now.date()
        )
        return context


class CourseListView(ListView):
    """
        Blogs List
    """
    queryset = CourseModel.active.filter()
    template_name = 'develawp/courses.html'
    paginate_by = 12
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    """
        Blogs List
    """
    queryset = CourseModel.active.filter()
    template_name = 'develawp/course.html'
    context_object_name = 'course'


def get_time_slots(request, *args, **kwargs):
    slug = kwargs.get('slug')
    if not request.GET.get('date', None):
        raise Http404

    course = get_object_or_404(
        CourseModel,
        slug=slug
    )
    # Extract the Time Slot
    # and add to context dictionary
    data_dict = {
        'timeslots': course.timeslots.filter(date=request.GET['date']).first().timeslots
    }

    return render(
        request,
        template_name="develawp/partials/time_slots.html",
        context=data_dict
    )


class SubscriptionWizardView(SessionWizardView):
    # TEMPLATES = {"address": "checkout/billingaddress.html",
    #              "paytype": "checkout/paymentmethod.html",
    #              "cc": "checkout/creditcard.html",
    #              "confirmation": "checkout/confirmation.html"}

    template_name = "develawp/subscription.html"

    form_list = [
        SubscriptionFormStep1,
        SubscriptionFormStep2
    ]
    #
    # def get_template_names(self):
    #     return [self.TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


class SubscriptionView(FormView):

    template_name = "develawp/includes/develawp_form.html"
    form_class = SubscriptionForm
    success_url = reverse_lazy("develawp_enquiry_form_thanks")

    def form_valid(self, form):
        print('here')
        form.save()
        return super().form_valid(form)
