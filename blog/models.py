from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.encoding import force_text

from imagekit.models import ProcessedImageField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from sortedm2m.fields import SortedManyToManyField
from taggit.managers import TaggableManager

from core.models import (
    AuditModel,
    SEOModel,
    StateModel
)


class BlogCategoryModel(
    MPTTModel,
    SEOModel,
    StateModel,
    AuditModel
):
    """
        Blog Categories
    """

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

    name = models.CharField(
        max_length=100,
        unique=True
    )
    slug = models.SlugField(unique=True)
    image = ProcessedImageField(
        upload_to="nullstack_technologies/blog-category/%Y/%m/%d",
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    information = models.CharField(max_length=2048, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    @property
    def generate_slug(self):
        ancestors = self.get_ancestors()
        return '/'.join([force_text(i.slug) for i in ancestors] + [self.slug, ]).strip()

    @property
    def arrow_repr(self):
        ancestors = self.get_ancestors()
        return ' > '.join([force_text(i.name) for i in ancestors] + [self.name, ])

    def get_absolute_url(self):
        return reverse('blog_category', args=[self.generate_slug])

    def __str__(self):
        return self.arrow_repr


class BlogModel(
    StateModel,
    AuditModel,
    SEOModel
):
    """
        Services provided in
        NullStack Technologies
    """

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = (
            'order',
        )

    title = models.CharField(
        max_length=200,
        unique=True
    )
    thumbnail_image = ProcessedImageField(
        upload_to="nullstack_technologies/services/%Y/%m/%d",
        format='JPEG',
        options={'quality': 90},
        null=True,
        blank=True,
    )
    featured = models.BooleanField(
        help_text="Should this blog be featured in the home page?",
        default=False
    )
    author = models.ForeignKey(
        'website.TeamModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Attach Team Member as Author of this Blog"
    )
    blog_category = models.ForeignKey(
        BlogCategoryModel,
        null=True,
        on_delete=models.SET_NULL,
    )
    service = models.ForeignKey(
        'website.ServiceModel',
        related_name='blogs',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Service that this entry is referring to"
    )
    order = models.IntegerField(default=1)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    tags = TaggableManager()
    similar_blogs = models.ManyToManyField(
        'self',
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])

    
    def get_related_objects(self, count=9):
        return BlogModel.active.exclude(pk=self.pk).filter(
            Q(service=self.service) |
            Q(pk__in=self.similar_blogs.all())
        ).distinct()[:count]


    # def clean(self):
    #     # if it is a main service, you have to set allow booking to true
    #     if not self.is_main_service and not self.allow_booking:
    #         raise ValidationError({
    #             'allow_booking': _('For Main Services have to allow Booking')
    #         })
