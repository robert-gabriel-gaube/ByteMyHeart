from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=25, null=False, unique=True, validators=[MinLengthValidator(8)])
    password = models.CharField(max_length=100, null=False)
    isBanned = models.BooleanField(default=False)
    role = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=1, null=False) #1 -> user
    matchId = models.OneToOneField('self', on_delete=models.CASCADE, null=True)
    formId = models.OneToOneField('form', on_delete=models.CASCADE, null=False)
