from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from blog.forms import BlogForm
from blog.models import (
    BlogModel, BlogCategoryModel
)

from adminsortable2.admin import SortableAdminMixin


@admin.register(BlogCategoryModel)
class BlogCategoryAdmin(MPTTModelAdmin):
    search_fields = ['name']
    mptt_indent_field = 'name'
    autocomplete_fields = ['parent']
    list_display = ['name', 'slug']
    prepopulated_fields = {
        "slug": ("name",),
    }
    readonly_fields = [
        'created_by',
        'updated_by'
    ]


@admin.register(BlogModel)
class BlogAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_filter = [
        'created_at',
        'updated_at',
        'blog_category'
    ]
    form = BlogForm
    fieldsets = (
        (
            'Basic Data',
            {
                'fields':
                    (
                        'title',
                        'author',
                        'thumbnail_image',
                        'blog_category',
                        'body',
                        # 'tags',
                        'featured',
                        'service',
                        'similar_blogs',
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
                    ),
                'classes': ('wide', 'extrapretty',),
            }
        )
    )
    list_display = [
        'pk',
        'order',
        'title',
        'blog_category',
        'author',
        'service',
        'status',
        'created_at',
    ]
    autocomplete_fields = ['blog_category']
    readonly_fields = [
        'created_by',
        'updated_by',
        'created_at',
        'updated_at'
    ]
    prepopulated_fields = {
        "slug": ("title",),
    }
    search_fields = ['title']
    filter_horizontal = [
        'similar_blogs',
    ]

