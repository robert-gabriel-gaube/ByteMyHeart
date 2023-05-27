from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=40, null=False)
    age = models.IntegerField(null=False, validators=[MinValueValidator(18)])
    programming_language = models.CharField(max_length=10, null=False)
    university_specialization = models.CharField(max_length=10, null=False)
    course_fav1 = models.CharField(max_length=10, null=False)
    course_fav2 = models.CharField(max_length=10, null=False)
    course_fav3 = models.CharField(max_length=10, null=False)
    hobby1 = models.CharField(max_length=15, null=False)
    hobby2 = models.CharField(max_length=15, null=False)
    hobby3 = models.CharField(max_length=15, null=False)
    hobby4 = models.CharField(max_length=15, null=False)
    hobby5 = models.CharField(max_length=15, null=False)
    UNKNOWN = "-"
    FEMININ = "F"
    MASCULIN = "M"
    GENDER_CHOICES = [
        (FEMININ, "FEMININ"),
        (MASCULIN, "MASCULIN")
    ]

    def is_upperclass(self):
        return self.GENDER_CHOICES in {self.FEMININ, self.MASCULIN}
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    interest = models.CharField(max_length=1, choices=GENDER_CHOICES)
    favorite_algorithm = models.CharField(max_length=15, null=False)
    favorite_data_structure = models.CharField(max_length=15, null=False)
    short_description = models.CharField(max_length=50, null=False)


class User(models.Model):
    username = models.CharField(max_length=25, null=False, unique=True, validators=[MinLengthValidator(8)])
    password = models.CharField(max_length=100, null=False)
    isBanned = models.BooleanField(default=False)
    role = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=1,
                               null=False)  # 1 -> user
    matchId = models.OneToOneField('self', on_delete=models.CASCADE, null=True)
    formId = models.OneToOneField(Form, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.username
    
class Report(models.Model):
    receiverID = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=300, blank=False, null=False)
    
    OPEN = "OPN"
    CLOSED = "CSD"

    STATUS_CHOICES = [
        (OPEN, "OPEN"),
        (CLOSED, "CLOSED")
    ]

    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=OPEN)

class DateOffer(models.Model):
    senderId = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='senderId')
    receiverId = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='receiverId')
    date_idea = models.CharField(max_length=300, null=False)
    date_time = models.TimeField(null=False)
    date_location = models.CharField(max_length=50, null=False)
    PENDING = "PND"
    ACCEPTED = "ACC"
    DECLINED = "DEC"
    STATUS_CHOICES = [
        (PENDING, "PENDING"),
        (ACCEPTED, "ACCEPTED"),
        (DECLINED, "DECLINED")
    ]
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
