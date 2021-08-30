from django.db import models
from colorfield.fields import ColorField
from django.db.models.fields import IntegerField

# Create your models here.
class ColourPic(models.Model):
    volume = IntegerField()
    colour = ColorField(default='#FF0000')


