from django.db import models

from accounts.models import User


class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
