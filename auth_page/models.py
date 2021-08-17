from django.db import models
from django.utils import timezone

class UserDtls(models.Model):
    username = models.CharField(max_length = 50,)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    date_joined = models.DateTimeField(default=timezone.now)