from django.db import models

# Create your models here.
class InviteCodes(models.Model):
    inviteCode = models.CharField(max_length=100)
