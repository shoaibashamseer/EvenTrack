from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File

class Customer(models.Model):
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

