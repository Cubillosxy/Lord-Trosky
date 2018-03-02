from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from . import serializers
from . import models


class PublicationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PublicationSerializer
    pagination_class = None

    def get_queryset(self):
        if (
            self.request.user.is_authenticated() and
            not self.request.user.is_superuser
        ):
            return models.Publication.objects.all()

        return models.Publication.objects.all()
