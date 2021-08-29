from django import forms
from .models import Question, Image

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['user']
        fields = ('title', 'text',)
 
 
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )