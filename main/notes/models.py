from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL, blank=True, null=True)
    note_name = models.CharField(max_length=100)
    note_description = models.TextField()