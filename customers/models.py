from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    second_phone = models.CharField(max_length=20)
    telegram = models.CharField(max_length=50)
