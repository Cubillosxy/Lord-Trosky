from django.contrib import admin
from .models import Article
from .models import Publication
from .models import Qualification

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'created_at', 'publication', 'user')
	search_fields = ('name', 'user__email', 'publication__title')
	raw_id_fields = ('user', )
	filters = ('created_at', )

class PublicationAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'created_at')
	search_fields = ('title', 'id')


class QualificationAdmin(admin.ModelAdmin):
	list_display = ('id', 'article', 'score', 'user')
	raw_id_fields = ('user', 'article')
	search_fields = ('article__id', 'article__name', 'user__email')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Qualification, QualificationAdmin)