from .models import Article, Author
from django.forms import ModelForm, TextInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]
        widgets = {
            "title": TextInput(attrs={
                "placeholder": "Write a theme"
                }),
            "content": Textarea(attrs={
                "placeholder": "Write a text"
            })
        }