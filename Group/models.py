from django.db import models

# Create your models here.
class Group(models.Model):
    #TODO:orginaziation many to many field
    name = models.TextField()
    description = models.TextField()
    group_image = models.ImageField(blank = True, null = True, upload_to = "media")
    def __str__(self):
        return str(self.name)
    def get_members(self):
        users = Membership.objects.filter(group = self)
        resultArray = []
        for x in users:
            resultArray.append(str(x.user))
        return resultArray


class Group_Protocol(models.Model):
    group = models.ForeignKey(Group, on_delete = "cascade")
    protocol = models.ForeignKey(Protocol, on_delete = "")
    def __str__(self):
        return str(self.group)