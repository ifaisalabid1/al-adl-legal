from django.urls import path, re_path
from django.views.generic import RedirectView

from blog.views import (
    BlogListView, BlogDetailView,
    BlogCategoryListView,
    BlogCategoryView, BlogTagListView,
    BlogAddView
)


urlpatterns = [
    path('add/', BlogAddView.as_view(), name="blog_api_add"),
    path('categories/', BlogCategoryListView.as_view(), name="blog_categories"),
    path('category/', RedirectView.as_view(url='/news/categories/', permanent=False)),
    # path('tag/', RedirectView.as_view(url='/news/categories/', permanent=False)),
    re_path(
        r'^category/(?P<path>.*)/',
        BlogCategoryView.as_view(),
        name='blog_category'
    ),
    # re_path(
    #     r'^tag/(?P<path>.*)/',
    #     BlogTagListView.as_view(),
    #     name='blog_tag'
    # ),

    path('', BlogListView.as_view(), name="blog_list"),
    re_path(
        r'(?P<path>.*)/',
        BlogDetailView.as_view(),
        name='blog_detail'
    ),
    # path('<slug:slug>/', BlogDetailView.as_view(), name="blog_detail"),
]
