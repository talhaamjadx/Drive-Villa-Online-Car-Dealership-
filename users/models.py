from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

# Create your models here.

class CustomUser(AbstractUser):
    customer_cnic = models.CharField(max_length = 13, default = '3520212453175')
    customer_dob = models.DateField(verbose_name = "Date of birth", default = datetime.date.today)
    # pass
