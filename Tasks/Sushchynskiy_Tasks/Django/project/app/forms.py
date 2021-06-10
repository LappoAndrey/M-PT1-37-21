from django import forms
from django.contrib.auth.models import User


class AddArticle(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form_title'}), max_length=100, label="Title", required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form_content'}), label="Content", required=True)
    image = forms.ImageField(label="Image", required=False)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']