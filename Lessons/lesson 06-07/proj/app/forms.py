from django import forms
from django.forms import fields
from .models import Post

# class AddPost(forms.Form):
    
#     title = forms.CharField(max_length=100, label='Title', required=True)
#     subtitle = forms.CharField(max_length=100, label='Subtitle', required=True)
#     content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'test'}), label='Content')
#     post_type = forms.ChoiceField(required=True, choices=Post.POST_TYPES, label='Post type')
#     image = forms.ImageField(label='Image')

#     def clean_title(self):

#         title_value = self.cleaned_data['title']
#         if 'http' in title_value:
#             raise forms.ValidationError('please do not insert stupid links in this field, thank you very much')

#         return title_value
        
class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'post_type', 'image')
        labels = {'image':"Your image:", 'title': 'title'}