from django import forms
from .models import User, Form

class BigRegisterForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'
        labels = {
            "name": "Name",
            "age": "Age",
            "programming_language": "Favorite Programming Language",
            "university_specialization": "Your specialization at the uni is",
            "course_fav1": "Fav course1",
            "course_fav2": "Fav course2",
            "course_fav3": "Fav course3",
            "hobby1": "First hobby",
            "hobby2": "Second hobby",
            "hobby3": "Third hobby",
            "hobby4": "Fourth hobby",
            "hobby5": "Fifth hobby",
            "gender": "Your gender",
            "interest": "You are interested in",
            "favorite_algorithm": "Favorite algorithm",
            "favorite_data_structure": "Favorite data structure",
            "short_description": "Your description",
        }
        error_messages = {
            "name": {
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "age": {
                "required": "This field must not be empty!"
            },
            "programming_language": {
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "course_fav1":{
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "course_fav2":{
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "course_fav3":{
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "hobby1": {
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "hobby2": {
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "hobby3": {
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "hobby4": {
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "hobby5": {
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "interest":{
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "favorite_algorithm":{
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "favorite_data_structure":{
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            },
            "short_description":{
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter text!"       
            }
        }

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
