# fire/models.py

from django.db import models
from tinymce.models import HTMLField


class Staff(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,primary_key=True)
    photo = models.ImageField(upload_to='staff_photos/')
    post = models.TextField()
    detail = HTMLField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'fire'

class Review(models.Model):
    name = models.CharField(max_length=250)
    review = models.TextField(max_length=5000)

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self):
        return self.name
