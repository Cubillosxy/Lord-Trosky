from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from . import serializers
from .models import Publication


class PublicationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PublicationSerializer
    pagination_class = None

    def get_queryset(self):
        if (
            self.request.user.is_authenticated and
            not self.request.user.is_superuser
        ):
            return Publication.objects.all()

        return Publication.objects.all()

    def retrieve(self, request, pk=None):
        publication = get_object_or_404(Publication, pk=pk)
        serializer = serializers.PublicationSerializer(publication)
        return Response(serializer.data)

    def create(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        if not title or not description:
            return Response({'ok': False, 'message': 'Incomplete Fields'})
        Publication.objects.create(title=title, description=description)
        return Response({'ok': True})
