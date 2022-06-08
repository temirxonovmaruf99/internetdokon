from django import forms
from django.core.exceptions import ValidationError
from .models import User


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=100, widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, max_length=20)
    last_name = forms.CharField(required=True, max_length=20)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'confirm')

        widgets = {
            'password': forms.PasswordInput
        }


    def clean(self):
        data = super().clean()

        if data.get("password") != data.get("confirm"):
            raise ValidationError({"confirm": "Parollar bir xil emas"})

        return data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


