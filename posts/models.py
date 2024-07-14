from django.db import models
from datetime import datetime
# Create your models here.

class posts(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    desc = models.CharField(max_length=700)