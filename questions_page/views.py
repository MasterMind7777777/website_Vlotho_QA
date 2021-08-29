from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, QuestionForm
from .models import Image

# Create your views here.

def questionMain_view(request):
    return render(request, 'questions_page/questions_main.html')

@login_required
def postQ_view(request):
 
    ImageFormSet = modelformset_factory(Image,
                                        form=ImageForm)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
    
        questionForm = QuestionForm(request.POST, request.user)
        formset = ImageFormSet(request.POST, request.FILES)

        if questionForm.is_valid() and formset.is_valid():
            question_obj = questionForm.save(commit=False)
            question_obj.user = request.user
            question_obj.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    Image.objects.create(image=image, question=question_obj)
            return HttpResponseRedirect('/')
        else:
            print(questionForm.errors, formset.errors)
    else:
        questionForm = QuestionForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(request, 'questions_page/postQ.html', {"questionForm":questionForm, "formset":formset})
    return render(request, 'questions_page/postQ.html',
                  {'questionForm': questionForm, 'formset': formset})