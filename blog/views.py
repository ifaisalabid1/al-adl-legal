from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.http.response import Http404

from blog.models import BlogModel, BlogCategoryModel
from .serializers import BlogSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from taggit.models import Tag


class BlogAddView(CreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class BlogListView(ListView):
    """
        Blogs List
    """
    queryset = BlogModel.active.filter()
    template_name = 'blog/blogs.html'
    paginate_by = 12
    context_object_name = 'blogs'


class BlogCategoryListView(ListView):
    """
        Blog Category List
    """
    queryset = BlogCategoryModel.active.all()
    template_name = 'blog/blog_categories.html'
    paginate_by = 50
    context_object_name = 'categories'


class BlogTagListView(ListView):
    """
        Blog Category List
    """
    queryset = Tag.objects.all()
    template_name = 'blog/blog_tags.html'
    paginate_by = 12
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

    def get_queryset(self):
        slug = self.request.path.split('/')
        self.tag = get_object_or_404(Tag, slug=slug[-2])
        return BlogModel.objects.filter(tags__in=[self.tag])


class BlogDetailView(DetailView):
    """
        Blogs Detail
    """
    queryset = BlogModel.active.all()
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = BlogCategoryModel.objects.order_by('?')[:10]
        context['categories'] = categories
        return context

    def get_object(self, queryset=None):
        slug = self.request.path.split('/')
        blog = None
        if queryset is None:
            queryset = self.get_queryset()
        for element in slug[slug.index('news') + 1:]:
            if element:
                try:
                    blog = queryset.get(slug=element)
                except:
                    raise Http404
        return blog


class BlogCategoryView(ListView):
    """
        Blog Category List
    """
    queryset = BlogCategoryModel.active.all()
    template_name = 'blog/blog_category.html'
    paginate_by = 12
    context_object_name = 'blogs'
    blog_category = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_category'] = self.blog_category
        return context

    def get_queryset(self):
        slug = self.request.path.split('/')
        self.blog_category = get_object_or_404(BlogCategoryModel, slug=slug[-2])
        return BlogModel.objects.filter(blog_category=self.blog_category)

        # blog_list = Blog.active.all()
        #
        # blogs_pk = []
        # for _ in blog_list:
        #     # check if blog is in the descendants,
        #     # then technically this blog also belongs to this category
        #     if _.blog_category == self.blog_category \
        #             or _.blog_category in self.blog_category.get_descendants()\
        #             or self.blog_category in _.blog_categories.all():
        #         blogs_pk.append(_.pk)
        #
        # blog_list = blog_list.filter(pk__in=blogs_pk)
        #
        # return blog_list
