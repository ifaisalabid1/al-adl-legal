from django.db import models
from django.conf import settings

from core.managers import StateModelManager, SecondStateModelManager

from imagekit.models import ProcessedImageField


class BaseModel(models.Model):
    """
        Base model for
        all the models.

        Some Operations that apply to all the tables
        may be placed over here.

        does nothing but lets all the other models
        extend it.
    """

    objects = models.Manager()

    class Meta:
        abstract = True

    @property
    def _pk(self):
        return f"⚙️ (Edit)"

    @property
    def _view(self):
        return f"👁️ (View)"


class AuditModel(BaseModel):
    """
        Audit Model for the whole project.

        This has the audit fields.
        viz(Namely): created_at, updated_at,
        created_by, updated_by.

        Will be extended by models needing to audit there
        status of saves and updates
    """

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )


class SlugModel(BaseModel):
    """
        Model to add slug field to a
        django model
    """
    class Meta:
        abstract = True

    slug = models.SlugField(max_length=256, unique=True, db_index=True)


class StateModel(BaseModel):
    """
        This models stores the state of a model.

        There are basically two states of every model
        1.) Active
        2.) Inactive

        A model entry can never be Deleted.
        It should always be deactivated
    """

    class Meta:
        abstract = True

    class StateChoices(models.TextChoices):
        ACTIVE = ('ACTIVE', 'Active')
        INACTIVE = ('INACTIVE', 'Inactive')

    objects = models.Manager()  # Default Manager
    active = StateModelManager()  # Custom Model Manager
    inactive = SecondStateModelManager()  # Custom Model Manager

    status = models.CharField(max_length=8, choices=StateChoices.choices, default=StateChoices.ACTIVE)

    def is_active(self):
        if self.status == self.StateChoices.ACTIVE:
            return True
        return False
    is_active.boolean = True

    def activate(self):
        self.status = self.StateChoices.ACTIVE

    def deactivate(self):
        self.status = self.StateChoices.INACTIVE


class SEOModel(BaseModel):

    class Meta:
        abstract = True

    seo_title = models.CharField(max_length=255, null=True, blank=True)
    seo_description = models.CharField(max_length=500, null=True, blank=True)
    seo_keywords = models.CharField(max_length=500, null=True, blank=True)
    seo_url = models.URLField(null=True, blank=True)
    seo_image = ProcessedImageField(
        upload_to="al_adl/images/%Y/%m/%d",
        format='JPEG',
        options={'quality': 60},
        null=True,
        blank=True
    )
    extra_seo_content = models.TextField(null=True, blank=True)
