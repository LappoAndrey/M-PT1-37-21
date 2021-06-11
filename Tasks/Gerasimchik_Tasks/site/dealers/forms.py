from django import forms
from .models import Dealer


class AddDealer(forms.ModelForm):

    class Meta:
        model = Dealer
        fields = '__all__'
