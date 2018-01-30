from django.db import models
from django.contrib.auth.models import User
# added
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
# TODO: Write the whole file
# connected to built in user but allow a picture
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserInfo(models.Model):
	user = models.OneToOneField(User, related_name='userinfo', on_delete = models.CASCADE)
	user_image = models.ImageField(blank = True, null = True, upload_to = "static/media")
	about = models.TextField(blank = True, null = True)
	contact_info = models.TextField(blank = True, null = True)
	is_verified = models.BooleanField(blank = False, default = False)

	def __str__(self):
		return str(self.user)

	def email(self):
		return self.user.email

	def is_admin(self):
		return self.user.is_staff

	def date_joined(self):
		return self.user.date_joined
