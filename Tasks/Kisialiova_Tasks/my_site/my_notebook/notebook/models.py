from django.conf import settings
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


COLORS = (
        ('a', 'yellow'),
        ('b', 'maroon'),
        ('c', 'lightseagreen'),
        ('d', 'red'),
        ('e', 'blue'),
        ('f', 'darkorange'),
        ('g', 'indigo')
    )


class Tags(models.Model):
    title = models.CharField(unique=True, max_length=240)

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return reverse('notes:tag_update', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('notes:tag_delete', kwargs={'pk': self.id})

    @staticmethod
    def filters_data(request, qs):
        q = request.GET.get('q', None)
        search_name = request.GET.get('search_name', None)

        qs = qs.filter(title__icontains=q) if q else qs
        qs = qs.filter(title__icontains=search_name) if search_name else qs
        return qs


class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pinned = models.BooleanField(default=False, verbose_name='Pinned')
    title = models.CharField(max_length=400, verbose_name='Title')
    description = RichTextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tags, blank=True)
    color = models.CharField(max_length=1, choices=COLORS, default='a', verbose_name='Color')

    class Meta:
        ordering = ['-pinned', '-timestamp']

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return reverse('notes:note_update', kwargs={'pk': self.id})

    def get_show_url(self):
        return reverse('notes:show_note', kwargs={'pk': self.id})

    @staticmethod
    def filters_data(request, qs):
        q = request.GET.get('q', None)
        tags = request.GET.getlist('tag', None)
        if tags:
            tags_ = Tags.objects.filter(id__in=tags)
            qs = qs.filter(tag__in=tags_)
        qs = qs.filter(title__icontains=q) if q else qs
        return qs