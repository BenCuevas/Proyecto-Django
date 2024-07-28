from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    pass


class  ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'