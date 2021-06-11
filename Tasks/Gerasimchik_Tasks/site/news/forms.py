from django import forms
from .models import Article
from ckeditor.widgets import CKEditorWidget


class AddPost(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ['title', 'slug', 'description', 'tags', 'text', 'image']
