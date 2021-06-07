from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'post_type', 'image', 'issued', 'author')