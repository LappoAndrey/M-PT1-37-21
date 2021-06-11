from django.contrib.admin.options import VERTICAL
from django.db import models

class Article(models.Model):
    
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    data = models.DateTimeField()
    image = models.ImageField(upload_to='uploads', blank=True)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=50, blank=False)
    avatar = models.ImageField(upload_to='uploads', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:

        verbose_name = "Author"
        verbose_name_plural = "Authors"

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)    
    author_name = models.CharField(max_length=50, blank=False)
    comment_text = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'{self.author_name}'