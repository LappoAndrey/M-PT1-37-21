from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.urls import reverse

    
class Nnews(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="uploads")

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.TextField(max_length=200)
    ans1 = models.CharField(max_length=100)
    ans2 = models.CharField(max_length=100)
    ans3 = models.CharField(max_length=100)
    key = models.IntegerField(default=1)

    class Meta:
        permissions = (('can_add_choice', 'Can add choice'), ('can_delete_choice', 'Can delete choice'))
    

    def __str__(self): 
        return self.question


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Choice, on_delete=models.CASCADE)
    result = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.question} - {self.result}"    