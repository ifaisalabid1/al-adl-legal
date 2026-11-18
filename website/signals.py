from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import EnquiryModel
from constance import config


@receiver(post_save, sender=EnquiryModel)
def send_email_to_user(sender, **kwargs):
    if kwargs['created']:
        msg_html = render_to_string('website/includes/enquiry_email.html', {'enquiry': kwargs['instance']})
        msg_txt = render_to_string('website/includes/enquiry_email.txt', {'enquiry': kwargs['instance']})
        send_mail(
            subject='Enquiry - Al Adl Website',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=config.COMPANY_ADMIN_EMAILS.split(','),
            message=msg_txt,
            html_message=msg_html,
        )
