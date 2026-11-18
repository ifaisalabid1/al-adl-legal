from django.urls import path, include
from django.views.generic import RedirectView

from .views import *
from .admin import *


urlpatterns = [
    path('admin/', develawp_admin.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),


    path('', HomePageView.as_view(), name="develawp_home"),
    # path('courses/', CourseListView.as_view(), name="devalawp_courses_lists"),
    # path('class-schedule/<slug:slug>/', get_time_slots, name="devalawp_courses_time_slots"),
    path('form/', SubscriptionView.as_view(), name="devalawp_subscription"),
    path(
        'enquiry-form-thank-you/',
        TemplateView.as_view(template_name="develawp/includes/develawp_enquiry_form_thanks.html"),
        name="develawp_enquiry_form_thanks"
    ),
    # path('<slug:slug>/', CourseDetailView.as_view(), name="devalawp_course_detail"),
]
