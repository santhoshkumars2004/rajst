from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # Add other fields as needed

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
