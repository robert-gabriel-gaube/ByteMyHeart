from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=40, null=False)
    age = models.IntegerField(null=False)
    programming_language = models.CharField(max_length=5, null=False)
    university_specialization = models.CharField(max_length=10, null=False)
    course_fav1 = models.CharField(max_length=6, null=False)
    course_fav2 = models.CharField(max_length=6, null=False)
    course_fav3 = models.CharField(max_length=6, null=False)
    hobby1 = models.CharField(max_length=15, null=False)
    hobby2 = models.CharField(max_length=15, null=False)
    hobby3 = models.CharField(max_length=15, null=False)
    hobby4 = models.CharField(max_length=15, null=False)
    hobby5 = models.CharField(max_length=15, null=False)
    UNKNOWN = "U"
    FEMININ = "F"
    MASCULIN = "M"
    GENDER_CHOICES = [
        (FEMININ, "FEMININ"),
        (MASCULIN, "MASCULIN"),
        (UNKNOWN, "UNKNOWN"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=UNKNOWN)
    interest = models.CharField(max_length=10, null=False)
    favorite_algorithm = models.CharField(max_length=15, null=False)
    favorite_data_structure = models.CharField(max_length=15, null=False)
    short_description = models.CharField(max_length=50, null=False)
    # def is_upperclass(self):
    #     return self.GENDER_CHOICES in {self.FEMININ, self.MASCULIN}


class User(models.Model):
    username = models.CharField(max_length=25, null=False, unique=True, validators=[MinLengthValidator(8)])
    password = models.CharField(max_length=100, null=False)
    isBanned = models.BooleanField(default=False)
    role = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=1,
                               null=False)  # 1 -> user
    matchId = models.OneToOneField('self', on_delete=models.CASCADE, null=True)
    formId = models.OneToOneField('form', on_delete=models.CASCADE, null=False)
