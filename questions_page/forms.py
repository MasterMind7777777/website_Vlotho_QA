from django import forms
from .models import Question, Image
from django.utils.translation import gettext_lazy as _

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        exclude = ['user']
        fields = ('title', 'text',)
        labels = {
           'title' : _('title'),
           'text' : _('text'),
        }
 
 
# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('image', )

class ImageForm(forms.Form):
    images = forms.FileField(label=_('images'), widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Image
        fields = ('image', )
