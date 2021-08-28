from django import forms
from .models import Question, Image

class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    text = forms.Textarea()
 
    class Meta:
        model = Question
        fields = ('title', 'text', )
 
 
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image') 

    class Meta:
        model = Image
        fields = ('image', )