from django.contrib import admin

from .forms import ServiceForm, TeamForm
from .models import *

from adminsortable2.admin import SortableAdminMixin


@admin.register(ServiceModel)
class ServiceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_filter = [
        'created_at',
        'updated_at',
    ]
    list_display = [
        'pk',
        'order',
        'title',
        'slug',
        'created_by',
        'updated_by'
    ]
    readonly_fields = [
        'created_by',
        'created_at',
        'updated_by',
        'updated_at',
    ]
    prepopulated_fields = {
        "slug": ("name",),
    }
    search_fields = ['title', 'description', 'body', 'name']
    form = ServiceForm
    fieldsets = (
        (
            'Basic Data',
            {
                'fields':
                    (
                        'name',
                        'title',
                        'description',
                        'short_description',
                        'image',
                        'thumbnail_image',
                        'youtube_link',
                        'body',
                        'similar_services'

                    ),
                'classes': ('wide', 'extrapretty',),
            }
        ),
        (
            'SEO Data',
            {
                'fields':
                    (
                        'slug',
                        'seo_title',
                        'seo_description',
                        'seo_keywords',
                        'extra_seo_content',
                    ),
                'classes': ('wide', 'extrapretty',),
            }
        ),
        (
            'Meta Data',
            {
                'fields':
                    (
                        'status',
                        'created_at',
                        'updated_at',
                        'updated_by',
                        'created_by',
                    ),
                'classes': ('wide', 'extrapretty', 'collapse'),
            }
        ),
        (
            'FAQs',
            {
                'fields':
                    (
                        'faqs',
                    ),
                'classes': ('wide', 'extrapretty',),
            }
        ),
        (
            'Team',
            {
                'fields':
                    (
                        'team',
                    ),
                'classes': ('wide', 'extrapretty',),
            }
        ),

    )


@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    form = TeamForm
    prepopulated_fields = {
        "slug": ("name",),
    }
    readonly_fields = [
        'created_by',
        'created_at',
        'updated_by',
        'updated_at',
    ]
    list_display = [
        'pk',
        'name',
        'designation',
    ]
    fieldsets = (
        (
            'Basic Data',
            {
                'fields':
                    (
                        'name',
                        'designation',
                        'image',
                        'bio',
                        'facebook_profile',
                        'instagram_profile',
                        'linkedin_profile',
                        'twitter_profile',
                    ),
                'classes': ('wide', 'extrapretty',),
            }
        ),
        (
            'Meta Data',
            {
                'fields':
                    (
                        'status',
                        'created_at',
                        'updated_at',
                        'updated_by',
                        'created_by',
                    ),
                'classes': ('wide', 'extrapretty', 'collapse'),
            }
        ),
        (
            'SEO Data',
            {
                'fields':
                    (
                        'slug',
                        'seo_title',
                        'seo_description',
                        'seo_keywords',
                        'extra_seo_content',
                    ),
                'classes': ('wide', 'extrapretty',),
            }
        )
    )


@admin.register(FAQModel)
class FAQAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = [
        'order',
        'pk',
        'question',
        'answer'
    ]
    readonly_fields = [
        'created_by',
        'created_at',
        'updated_by',
        'updated_at',
    ]


@admin.register(EnquiryModel)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'type_of_query', 'service', 'query', 'created_at']
    search_fields = ['name', 'phone_number', 'query']
    list_filter = ['created_at', 'type_of_query', 'service']


admin.site.site_header = "Website Admin | Al Adl | العدل"
admin.site.site_title = "Website Admin | Al Adl | العدل"
admin.site.index_title = "Website Admin | Al Adl | العدل"
