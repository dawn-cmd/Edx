from django.db import models
from django.utils import timezone

# Create your models here.
class ans(models.Model):
    num = models.IntegerField()
    timestamp = models.DateTimeField("Create time", default=timezone.now)