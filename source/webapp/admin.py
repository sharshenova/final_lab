from django.contrib import admin
from webapp.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author', 'created_at']


admin.site.register(Article, ArticleAdmin)
