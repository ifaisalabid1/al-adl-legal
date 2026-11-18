"""
    al_adl_website URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views
from django.views.generic import TemplateView, RedirectView
from django.contrib.sitemaps.views import sitemap

from al_adl_website.sitemap import sitemaps


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # sitemap and robots.txt URLS
    path('sitemap.xml', RedirectView.as_view(url='/sitemap_index.xml', permanent=False)),
    path('sitemap_index.xml', views.index, {'sitemaps': sitemaps}, name="sitemap"),
    path(
        '<section>-sitemap.xml',
        sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),

    path('develawp/', include('develawp.urls')),
    path('', include('website.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
