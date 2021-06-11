from django.contrib.auth.forms import UserCreationForm, User
from django.forms.widgets import EmailInput, TextInput
from .models import *
from django import forms
from django.forms import ModelForm, Textarea


# class TaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ["title", "task"]
        
#         widgets = {
#             "title": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter the question'
#             }),
#             "task": Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter answer ortions, e.g.:\n 1. Option1 \n 2. Option2'        
#             }),
#             }

class SigUpForm(UserCreationForm):
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    CHOICES = [('Professors', 'Professor'), ('Students', 'Student')]
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
       
    class Meta:
        model = User
        fields = ("status", "email", "first_name", "last_name", "username", "password1", "password2")


class AddquestionsForm(forms.ModelForm):
    # CHOICES = [('ans1', 'ans1'), ('ans2', 'ans2'), ('ans3', 'ans3')]
    # select_of_user = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model = Choice
        fields = ['question', 'ans1', 'ans2', 'ans3', 'key']


# class Result(forms.ModelForm):
#     class Meta:
#         model = Result
#         fields = ['result']



