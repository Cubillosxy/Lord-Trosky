from django.views.generic import TemplateView
from django.views import generic

from blog.models import Article


class BlogPageView(TemplateView):
    template_name = 'blogs.html'


class IndexView(generic.ListView):
    context_object_name = 'articles'
    template_name = 'latest_articles.html'

    def get_queryset(self):
        return Article.objects.order_by('-created_at')[:5]


class DetailView(generic.DetailView):
    """docstring for  DetailView"""
    model = Article
    template_name = 'article_detail.html'


class DeleteView(generic.DeleteView):
    model = Article
