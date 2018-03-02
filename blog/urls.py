from django.urls import path, include
from rest_framework import routers

from .viewsets import PublicationViewSet

router = routers.DefaultRouter()
router.register(r'publication', PublicationViewSet, base_name="publications")

urlpatterns = [
    path('', include(router.urls)),
]
