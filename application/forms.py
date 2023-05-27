from django import forms
from .models import User, Form, Report, DateOffer   

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput)

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

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['receiverID', 'description']
        labels = {
               'receiverID': 'Person to report',
               'description': 'Description of the report',
        }
        error_messages = {
            "receiverID": {
                "required": "This field must not be empty!",
            },
            "description": {
                "required": "This field must not be empty!",
                "max_length": "Please enter a shorter description!"
            }
        }

class DateOfferForm(forms.ModelForm):
    class Meta:
        model = DateOffer
        fields = ['date_idea', 'date_time', 'date_location']
        labels = {
                'date_idea': 'Date idea',
                'date_time': 'Date time',
                'date_location': 'Date location',
        }
        error_messages = {
            "date_idea": {
                "required": "This field must not be empty!",
            },
            "date_time": {
                "required": "This field must not be empty!",
            },
            "date_location": {
                "required": "This field must not be empty!",
            },
        }

class EditMyProfileForm(forms.Form):
    UNKNOWN = "-"
    FEMININ = "F"
    MASCULIN = "M"
    GENDER_CHOICES = [
        (FEMININ, "FEMALE"),
        (MASCULIN, "MALE")
    ]

    name = forms.CharField(label="Name", max_length=40)
    age = forms.IntegerField(label="Age")
    programming_language = forms.CharField(label="Favorite Programming Language", max_length=10)
    university_specialization = forms.CharField(label="Your specialization at the uni is", max_length=10)
    course_fav1 = forms.CharField(label="Fav course1", max_length=10)
    course_fav2 = forms.CharField(label="Fav course2", max_length=10)
    course_fav3 = forms.CharField(label="Fav course3", max_length=10)
    hobby1 = forms.CharField(label="First hobby", max_length=15)
    hobby2 = forms.CharField(label="Second hobby", max_length=15)
    hobby3 = forms.CharField(label="Third hobby", max_length=15)
    hobby4 = forms.CharField(label="Fourth hobby", max_length=15)
    hobby5 = forms.CharField(label="Fifth hobby", max_length=15)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    interest = forms.ChoiceField(choices=GENDER_CHOICES)
    favorite_algorithm = forms.CharField(label="Favorite algorithm", max_length=30)
    favorite_data_structure = forms.CharField(label="Favorite data structure", max_length=30)
    short_description = forms.CharField(label="Your description", max_length=50)

    def __init__(self, *args, **kwargs):
        super(EditMyProfileForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['age'].required = False
        self.fields['programming_language'].required = False
        self.fields['university_specialization'].required = False
        self.fields['course_fav1'].required = False
        self.fields['course_fav2'].required = False
        self.fields['course_fav3'].required = False
        self.fields['hobby1'].required = False
        self.fields['hobby2'].required = False
        self.fields['hobby3'].required = False
        self.fields['hobby4'].required = False
        self.fields['hobby5'].required = False
        self.fields['gender'].required = False
        self.fields['interest'].required = False
        self.fields['favorite_algorithm'].required = False
        self.fields['favorite_data_structure'].required = False
        self.fields['short_description'].required = False
        