from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, \
    CommentCreateView, CommentUpdateView, CommentDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('articles/<int:pk>/addcomment', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/edit', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment_delete'),

]
