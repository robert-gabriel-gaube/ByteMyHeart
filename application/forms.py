from django import forms
from .models import User, Form


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            "username": "Username",
            "password": "Password"
        }
        error_messages = {
            "username": {
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter name!"
            },
            "password": {
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter password!"
            }
        }
