from django.contrib.sitemaps import Sitemap, GenericSitemap
from django.urls import reverse

from website.models import ServiceModel
from blog.models import BlogModel, BlogCategoryModel


class StaticPagesSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return [
            'home',
            'about-us',
            'contact-us',
            'services',
            'faqs',
            'legal-team',
            'search',
            'blog_list',
            'blog_categories',
        ]

    def location(self, item):
        return reverse(item)


sitemaps = {
    'pages': StaticPagesSitemap,
    'services': GenericSitemap({
        'queryset': ServiceModel.active.all(),
        'date_field': 'updated_at',
    }, protocol='https'),
    'blog': GenericSitemap({
        'queryset': BlogModel.active.all(),
        'date_field': 'updated_at',
    }, protocol='https'),
    'blog-categories': GenericSitemap({
        'queryset': BlogCategoryModel.active.all(),
        'date_field': 'updated_at',
    }, protocol='https'),
}
