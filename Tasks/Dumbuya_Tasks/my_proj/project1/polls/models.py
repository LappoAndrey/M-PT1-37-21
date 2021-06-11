from django.db import models
from django.db.models.fields.files import ImageField
from django.utils import timezone


class SelfDescription(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='media')


    def __str__(self) :
        return self.name


class LampType1(models.Model):
    title = models.CharField(max_length=40)
    discription = models.TextField()
    image = ImageField(upload_to='media')

class LampType2(models.Model):
    title = models.CharField(max_length=40)
    discription = models.TextField()
    image = ImageField(upload_to='media')


class LampType3(models.Model):
    title = models.CharField(max_length=40)
    discription = models.TextField()
    image = ImageField(upload_to='media')

