from django.urls import path, include
from rest_framework import routers

from .viewsets import PublicationViewSet
from .views import BlogPageView

router = routers.DefaultRouter()
router.register(r'publication', PublicationViewSet, base_name="publications")

urlpatterns = [
    path('', include(router.urls)),
    path('principal', BlogPageView.as_view(), name='blogs'),
]
