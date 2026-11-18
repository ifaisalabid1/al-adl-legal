import json

from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

from core.models import StateModel, AuditModel, SEOModel, SlugModel

from imagekit.models import ProcessedImageField
from sortedm2m.fields import SortedManyToManyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from djmoney.models.fields import MoneyField
from django_better_admin_arrayfield.models.fields import ArrayField


class AffiliateModel(
    StateModel,
    AuditModel,
):
    """
        Affiliate Model to
        track the Affiliate Marketing links and
        rewards earned by Affiliates
    """
    class Meta:
        verbose_name = "Affiliate"
        verbose_name_plural = "Affiliates"

    name = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    affiliate_code = models.CharField(max_length=50, unique=True, db_index=True)

    def __str__(self):
        return self.name


class CourseModel(
    StateModel,
    AuditModel,
    SlugModel,
    SEOModel
):
    class CourseType(models.TextChoices):
        WEBINAR = "WEBINAR", "Webinar"
        WEBINAR_WITH_MATERIAL = "WEB_MATERIAL", "Webinar Material"

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = (
            'order',
        )

    name = models.CharField(
        max_length=200,
        unique=True
    )
    title = models.CharField(
        max_length=200,
    )
    featured = models.BooleanField(default=False)
    type_of_webinar = models.CharField(
        max_length=20,
        db_index=True,
        choices=CourseType.choices,
        default=CourseType.WEBINAR
    )
    image = ProcessedImageField(
        upload_to="al_adl/services/%Y/%m/%d",
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True,
    )
    duration = models.CharField(
        max_length=2,
        default=1,
        help_text="Duration of The Course in minutes"
    )
    material = models.FileField(
        upload_to="al_adl/develawp/materials/%Y/%m/%d",
        null=True,
        blank=True
    )
    material_price = MoneyField(
        max_digits=14, decimal_places=2,
        validators=[MinMoneyValidator(1)],
        default_currency='INR',
        null=True,
        blank=True
    )
    thumbnail_image = ProcessedImageField(
        upload_to="al_adl/services/%Y/%m/%d",
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True,
    )
    price = MoneyField(
        max_digits=14, decimal_places=2,
        validators=[MinMoneyValidator(1)],
        default_currency='INR'
    )
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    order = models.IntegerField(default=1)
    short_description = models.CharField(max_length=500, null=True, blank=True)
    body = models.TextField()
    faqs = SortedManyToManyField('develawp.FAQModel', blank=True)

    @property
    def available_classes(self):
        return self.timeslots.filter(
            date__gte=timezone.now()
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course', args=[self.slug])


class FAQModel(
    StateModel,
    AuditModel,
):

    class Meta:
        verbose_name = "Frequent Asked Question"
        verbose_name_plural = "Frequently Asked Questions"
        ordering = ('order', '-created_at')

    question = models.CharField(max_length=512)
    answer = models.CharField(max_length=1024)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.question


class ClassesModel(
    AuditModel
):
    """
        Time Slots in accordance to a date
    """

    class Meta:
        verbose_name = "Time Slot"
        verbose_name_plural = "Time Slots"
        ordering = (
            'date',
        )

    course = models.ForeignKey(
        CourseModel,
        on_delete=models.CASCADE,
        null=True,
        related_name='timeslots'
    )
    date = models.DateField()
    timeslots = ArrayField(
        models.TimeField(
            help_text="TIME IN 24 Hours Format e.g. 18:00 for 6 PM"
        ),
        size=5, null=True
    )

    def __str__(self):
        return f"{self.date}"


class SubscriptionModel(
    StateModel,
    AuditModel,
):

    class PaymentStatus(models.TextChoices):
        PAID = "PAID", "Paid"
        PENDING = "PENDING", "Pending"
        CANCELLED = "CANCELLED", "Cancelled"

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    course = models.ForeignKey(
        CourseModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name="slots"
    )
    name = models.CharField(
        'Name',
        max_length=50,
    )
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(
        'Phone Number',
        max_length=12,
    )
    payment_status = models.CharField(
        max_length=20,
        db_index=True,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING
    )
    payment_data = models.JSONField(
        default=None
    )
    datetime = models.DateTimeField(
        null=True,
        blank=True
    )
    affiliate_code = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
