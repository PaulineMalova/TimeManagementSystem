from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	username = models.CharField(max_length = 30)
	email = models.EmailField()
	profile_picture = models.ImageField(upload_to = "profile_pictures", blank=True)
	