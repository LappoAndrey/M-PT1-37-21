from django import forms
from .models import Comments,Author,Post
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author','text',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        labels = {'title': 'title'}



class UserAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name','date_of_birth',)

