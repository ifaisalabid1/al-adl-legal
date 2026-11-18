from django.db import models
from django.shortcuts import reverse
from imagekit.models import ProcessedImageField
from sortedm2m.fields import SortedManyToManyField

from core.models import AuditModel, SEOModel, SlugModel, StateModel


class TeamModel(SlugModel, StateModel, AuditModel, SEOModel):
    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ("-created_at",)

    name = models.CharField(
        max_length=200,
    )
    designation = models.CharField(max_length=200)
    image = ProcessedImageField(
        upload_to="al_adl/team/%Y/%m/%d",
        format="JPEG",
        options={"quality": 90},
        null=True,
        blank=True,
    )
    bio = models.CharField(max_length=2048, null=True, blank=True)
    facebook_profile = models.URLField(null=True, blank=True)
    instagram_profile = models.URLField(null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)
    twitter_profile = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class FAQModel(
    StateModel,
    AuditModel,
):
    class Meta:
        verbose_name = "Frequent Asked Question"
        verbose_name_plural = "Frequently Asked Questions"
        ordering = ("order", "-created_at")

    question = models.CharField(max_length=512)
    answer = models.CharField(max_length=1024)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.question


class ServiceModel(StateModel, AuditModel, SlugModel, SEOModel):
    """
    Services provided in
    Al Adl
    """

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ("order",)

    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(
        max_length=200,
    )
    image = ProcessedImageField(
        upload_to="al_adl/services/%Y/%m/%d",
        format="JPEG",
        options={"quality": 90},
        null=True,
        blank=True,
    )
    thumbnail_image = ProcessedImageField(
        upload_to="al_adl/services/%Y/%m/%d",
        format="JPEG",
        options={"quality": 90},
        null=True,
        blank=True,
    )
    youtube_link = models.URLField(null=True, blank=True)
    order = models.IntegerField(default=1)
    description = models.TextField(
        null=True, blank=True, help_text="Hero section description"
    )
    short_description = models.CharField(max_length=500, null=True, blank=True)
    body = models.TextField()
    faqs = SortedManyToManyField("website.FAQModel", blank=True)
    team = SortedManyToManyField("website.TeamModel", blank=True)
    similar_services = SortedManyToManyField("self", related_name="+")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("service", args=[self.slug])

    @property
    def youtube_embed_url(self):
        if not self.youtube_link:
            return None
        url = self.youtube_link.strip()
        if "youtube.com/embed/" in url:
            return url
        import re

        match = re.search(
            r"(?:youtu\.be\/|v=|\/embed\/|\/shorts\/|\/v\/)([a-zA-Z0-9_-]{11})",
            url,
        )
        if match:
            return f"https://www.youtube.com/embed/{match.group(1)}"
        return url


class EnquiryModel(AuditModel):
    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"

    ENQUIRY = "Enquiry"
    CAREER = "Career"
    COMPLAIN = "Complain"
    OTHER = "Other"
    TYPES_OF_QUERY = (
        (ENQUIRY, ENQUIRY),
        (CAREER, CAREER),
        (COMPLAIN, COMPLAIN),
        (OTHER, OTHER),
    )

    ip = models.GenericIPAddressField(null=True, blank=True)
    name = models.CharField(
        "Name",
        max_length=50,
    )
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(
        "Phone Number",
        max_length=15,
    )
    type_of_query = models.CharField(
        choices=TYPES_OF_QUERY, max_length=12, default=ENQUIRY
    )
    service = models.ForeignKey(
        ServiceModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    query = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name
