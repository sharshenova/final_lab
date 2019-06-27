from django.contrib import admin
from webapp.models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'author', 'created_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'text', 'author', 'created_at']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)