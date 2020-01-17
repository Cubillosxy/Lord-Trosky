from django.contrib import admin
from interview.models import Tag
from interview.models import Category
from interview.models import Question


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name', )


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_trunc', 'answer_trunc', 'created_at')
    search_fields = ('title', )
    list_filter = ('category', 'tags', 'is_active')
    raw_id_fields = ('category',)

    @staticmethod
    def title_trunc(obj):
        return obj.title[:90]

    @staticmethod
    def answer_trunc(obj):
        return obj.answer[:60]


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
