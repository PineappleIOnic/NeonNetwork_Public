from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email

    docfile = models.FileField(upload_to='static/users/',)

#class Document(models.Model):
#    docfile = models.FileField(upload_to='static/users/')

class Friendship(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(CustomUser, related_name="friendship_creator_set", on_delete=models.CASCADE)
    friend = models.ForeignKey(CustomUser, related_name="friend_set", on_delete=models.CASCADE)
