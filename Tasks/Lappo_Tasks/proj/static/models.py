from django.db import models

class Post(models.Model):

    POST_TYPES = [('C', 'Commercial'), ('A', 'Author'), ('P', 'Public Licinse')]
    
    title = models.CharField(max_length=100, blank=False)
    subtitle = models.CharField(max_length=100)
    content = models.TextField(blank=False)
    post_type = models.CharField(max_length=1, blank=False, choices=POST_TYPES)
    issued = models.DateTimeField()
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    

class Author(models.Model):

    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    avatar = models.ImageField(upload_to='uploads')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'