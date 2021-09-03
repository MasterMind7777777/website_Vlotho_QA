from django.db import models
from colorfield.fields import ColorField
from django.db.models.fields import CharField, FloatField, IntegerField

# Create your models here.
class ColourPic(models.Model):
    volume = IntegerField()
    colour = ColorField(default='#FF0000')

class ColourCatalog(models.Model):
    colour_id = CharField(max_length=15)
    hex = CharField(max_length=7, null=True)
    base_type = CharField(max_length=24)

    colour1 = CharField(max_length=3)
    colour2 = CharField(max_length=3)
    colour3 = CharField(max_length=3)
    colour4 = CharField(max_length=3)

    colour1_grams = FloatField()
    colour2_grams = FloatField()
    colour3_grams = FloatField()
    colour4_grams = FloatField()
