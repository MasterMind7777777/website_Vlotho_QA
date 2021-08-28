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
                                        form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
    
        questionForm = QuestionForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Image.objects.none())
    
    
        if questionForm.is_valid() and formset.is_valid():
            question_form = questionForm.save(commit=False)
            question_form.user = request.user
            question_form.save()
    
            for form in formset.cleaned_data:
                #this helps to not crash if the user   
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Image(post=question_form, image=image)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(questionForm.errors, formset.errors)
    else:
        questionForm = QuestionForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'questions_page/postQ.html',
                  {'questionForm': questionForm, 'formset': formset})