from django.contrib import admin
from .models import Post, Author, User, Comments

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'date_of_birth']

admin.site.register(Author, ProfileAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','creation')
    search_fields = ['title', 'text']

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'creation','active')
    list_filter = ('active','creation',)
    search_fields = ('author','text',)
admin.site.register(Comments, CommentAdmin)

