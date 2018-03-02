from rest_framework import serializers

from user.models import User

from .models import Publication
from .models import Article
from .models import Qualification


class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    publication = PublicationSerializer(many=False, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class QualificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    article = ArticleSerializer(many=False, read_only=True)

    class Meta:
        model = Qualification
        fields = '__all__'
