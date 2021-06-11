from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):

	creation = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
	text = models.TextField(max_length=1000)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/blog/%i/" % self.id

class Comments(models.Model):
	post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	text = models.TextField(max_length=1000)
	creation = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ['creation',]


	def __str__(self):
		return 'Comment by {} on {}'.format(self.author, self.post)



class Author(models.Model):

	username = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)


	def get_absolute_url(self):
		return self.id

	def __str__(self):
		return 'Profile for user {}'.format(self.username.username)