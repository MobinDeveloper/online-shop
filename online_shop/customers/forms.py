from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from core.models import User
from customers.models import Address


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['phone', 'password1', 'password2', 'password']

    password = forms.CharField(max_length=13, required=False)
    username = forms.CharField(max_length=13, required=False)

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.username = obj.phone
        if commit:
            obj.save()
        return obj


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        exclude = ['customer']
