from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    PROFILE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]
    profile_type = models.CharField(max_length=10, choices=PROFILE_CHOICES)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)