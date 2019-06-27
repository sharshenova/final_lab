from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
]
