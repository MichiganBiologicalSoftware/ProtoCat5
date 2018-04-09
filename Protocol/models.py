from django.db import models
from User.models import UserInfo
# Create your models here.

class Protocol(models.Model):
    """Class Docstring"""
    title = models.TextField()
    description = models.TextField()
    materials = models.TextField()
    author = models.ForeignKey(UserInfo, related_name="protocols")
	
