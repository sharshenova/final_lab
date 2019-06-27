from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Текст статьи")
    author = models.ForeignKey(User, blank=True, verbose_name="Автор", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article_images', blank=True, null=True, verbose_name="Картинка")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время создания")

    def __str__(self):
        return f"{self.pk}. {self.title} | {self.author.username}"

    def get_absolute_url(self):
        return reverse('webapp:article_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
