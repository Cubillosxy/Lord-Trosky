from django.views.generic import TemplateView


class BlogPageView(TemplateView):
    template_name = 'blogs.html'
