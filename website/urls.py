"""
al_adl_website URL Configuration
"""

from django.urls import path, include
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("search/", SearchView.as_view(), name="search"),
    path("services/", ServicesView.as_view(), name="services"),
    path("services/api/", ServicesAPIView.as_view(), name="services_api"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),
    path(
        "trademark-registration/",
        TrademarkRegistrationView.as_view(),
        name="trademark_registration",
    ),
    path("contact-us/", ContactUsView.as_view(), name="contact-us"),
    path("develawp/", include("develawp.urls"), name="develawp"),
    path("frequently-asked-questions/", FAQView.as_view(), name="faqs"),
    path("legal-team/", LegalTeamView.as_view(), name="legal-team"),
    path(
        "legal-team/<slug:slug>/",
        TeamMemberView.as_view(),
        name="legal-team-individual",
    ),
    path("enquiry-form/", EnquiryFormView.as_view(), name="enquiry_form"),
    path(
        "enquiry-form-thank-you/",
        TemplateView.as_view(template_name="website/includes/thank_you.html"),
        name="enquiry_form_thanks",
    ),
    path("news/", include("blog.urls")),
    path("<slug:slug>/", ServiceView.as_view(), name="service"),
]
