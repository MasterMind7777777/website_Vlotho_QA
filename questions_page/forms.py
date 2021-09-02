from django import forms
from .models import Question, Image, Answer, MediaFile
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

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        exclude = ['user']
        fields = ('title', 'text',)
        labels = {
           'title' : _('title'),
           'text' : _('text'),
        }


class ImageForm(forms.Form):
    images = forms.FileField(required=False, label=_('images'), widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Image
        fields = ('image', )


class MediaFileForm(forms.Form):
    media_files = forms.FileField(required=False, label=_('video, photo'), widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Image
        fields = ('media_file', )