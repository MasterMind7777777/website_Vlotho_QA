from .models import ColourPic
from django import forms
from django.utils.translation import gettext_lazy as _

class ColourForm(forms.ModelForm):
    
    class Meta:
        model = ColourPic
        fields = (('volume'), ('colour'), )
        labels = {
           'volume' : _('Volume in milliliters'),
           'colour' : _('colour'),
        }

 