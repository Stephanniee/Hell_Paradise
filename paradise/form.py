from django import forms
from .models import Merch
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Form(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        model = Merch
        fields = ['name', 'price', 'description', 'image']
