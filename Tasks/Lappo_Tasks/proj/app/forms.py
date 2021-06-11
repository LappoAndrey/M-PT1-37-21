from django import forms
from .models import USERS






# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
#
#     class Meta:
#         model = USERS
#         fields = ('login', 'idfirm', 'email')
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Пароли не совпадают!')
#         return cd['password2']
#
#
# class FilterFirms(forms.Form):
#
#     FILTER_CHOICES = (
#         ('time', 'Time'),
#
#     )
#
#     filter_by = forms.ChoiceField(choices = FILTER_CHOICES)
#
#







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
        