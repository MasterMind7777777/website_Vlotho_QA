from .models import ColourPic
from django import forms

class ColourForm(forms.ModelForm):
    volume = forms.IntegerField(label='Volume in milliliters')

    class Meta:
        model = ColourPic
        fields = ('volume', 'colour', )

