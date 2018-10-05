from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from . import serializers
from .models import Publication


class PublicationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PublicationSerializer
    queryset = Publication.objects.all()
    pagination_class = None

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
