from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Career(models.Model):
    student = models.CharField(max_length=100)
    mail_id = models.TextField()
    ph = models.TextField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
