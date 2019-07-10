from django.db import models
from user.models import User

# Create your models here.

class Task(models.Model):
	task_name = models.CharField(max_length = 200)
	start_date = models.DateField()
	planned_duration_in_days = models.SmallIntegerField()
	end_date = models.DateField()
	actual_duration_in_days = models.SmallIntegerField()
	user_name = models.ForeignKey(User, on_delete = models.CASCADE)