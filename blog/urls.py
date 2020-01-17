from django.urls import path, include
from rest_framework import routers

from .viewsets import PublicationViewSet
from .views import BlogPageView
from .views import IndexView
from .views import DetailView

router = routers.DefaultRouter()
router.register(r'publication', PublicationViewSet, base_name="publications")

urlpatterns = [
    path('', include(router.urls)),
    path('principal', BlogPageView.as_view(), name='blogs'),
    path('latest', IndexView.as_view(), name='latest'),
    path('article-detail/<int:pk>', DetailView.as_view(), name='article_detail'),
]
