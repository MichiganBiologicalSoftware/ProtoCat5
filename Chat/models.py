from django.db import models
from User.models import UserInfo

# Create your models here.
class Message(models.Model):
	sender = models.ForeignKey(UserInfo, related_name="sender_user")
	recipient = models.ForeignKey(UserInfo, related_name="recip_user")
	message = models.TextField()
	timeSent = models.DateTimeField(null = True, auto_now_add = True)
	deleted = models.BooleanField(default = False)
	read = models.BooleanField(default = False)

	def __str__(self):
		return self.sender.username + " to " + self.recipient.username