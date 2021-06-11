from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, blank=False, verbose_name='URL')
    description = models.TextField(blank=False, verbose_name='Короткое содержание')
    tags = models.CharField(max_length=100, blank=False, verbose_name='Тэги для SEO')
    text = RichTextUploadingField(blank=False)
    image = models.ImageField(verbose_name='Картинка на главную')
    datetime = models.DateTimeField(auto_now_add=True)
    datetime_modify = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = 'datetime'
        ordering = ['-datetime']
