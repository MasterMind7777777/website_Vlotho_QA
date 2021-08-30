from .models import ColourPic
from django import forms
from django.utils.translation import gettext_lazy as _

class ColourForm(forms.ModelForm):
    volume = forms.IntegerField(label=_('Volume in milliliters'))
    
    class Meta:
        model = ColourPic
        fields = (('volume'), ('colour'), )

 