from django.contrib import admin
from django import forms
from django.contrib.admin import AdminSite
from django.utils.html import format_html

from .forms import CourseForm
from .models import *

from adminsortable2.admin import SortableAdminMixin
from django_better_admin_arrayfield.forms.widgets import DynamicArrayWidget
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class DevelawpSite(AdminSite):
    site_header = "Develawp Admin"
    site_title = "Develawp Admin"
    index_title = "Welcome to Develawp Admin Portal"


develawp_admin = DevelawpSite(name='develawp_admin')


# @admin.register(AffiliateModel)
class AffiliateAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'affiliate_code', 'affilate_link']
    prepopulated_fields = {'affiliate_code': ('name',), }
    readonly_fields = ['created_by', 'updated_by']
    search_fields = ['name', 'email', 'affiliate_code']

    def affilate_link(self, obj):
        return format_html(f'<a href="https://develawp.aladllegal.com?aid={obj.affiliate_code}">https://develawp.aladllegal.com?aid={obj.affiliate_code}</a>')

    affilate_link.short_description = 'Affiliate Link'
    affilate_link.allow_tags = True


class TimeDynamicArrayWidget(DynamicArrayWidget):
    subwidget_form = forms.TextInput()


class ClassInline(admin.TabularInline, DynamicArrayMixin):
    model = ClassesModel
    extra = 0
    readonly_fields = [
        'created_by',
        'created_at',
        'updated_by',
        'updated_at',
    ]
    formfield_overrides = {
        'timeslots': {
            'widget': TimeDynamicArrayWidget(
                subwidget_form=forms.TextInput(
                    attrs={
                        'type': 'time',
                    }
                ),
            )
        },
    }


@admin.register(CourseModel)
class CourseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'title', 'type_of_webinar', 'price']
    # inlines = [ClassInline]
    form = CourseForm
    readonly_fields = [
        'created_by',
        'created_at',
        'updated_by',
        'updated_at',
    ]
    prepopulated_fields = {
        "slug": ("name",),
    }
    search_fields = ['title', 'body', 'name']

    fieldsets = (
        (
            'Basic Data',
            {
                'fields':
                    (
                        'name',
                        'title',
                        'date',
                        'time',
                        # 'image',
                        # 'featured',
                        # 'type_of_webinar',
                        'thumbnail_image',
                        'price',
                        'duration',
                        'short_description',
                        'body',

                    ),
                'classes': ('wide', 'extrapretty',),
            }
        ),
        (
            'Study Material',
            {
                'fields':
                    (
                        'material',
                        'material_price',
                    ),
                'classes': ('wide', 'extrapretty',),
            }
        ),
        (
            'FAQS',
            {
                'fields':
                    (
                        'faqs',
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
    )


@admin.register(SubscriptionModel)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone_number',
        'datetime',
        'created_at'
    ]
    list_filter = [
        'datetime',
        'created_at'
    ]
    search_fields = [
        'name__icontains',
        'phone_number__contains',
        'email__icontains'
    ]


# @admin.register(FAQModel)
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


develawp_admin.register(AffiliateModel, AffiliateAdmin)
develawp_admin.register(CourseModel, CourseAdmin)
develawp_admin.register(SubscriptionModel, SubscriptionAdmin)
develawp_admin.register(FAQModel, FAQAdmin)
