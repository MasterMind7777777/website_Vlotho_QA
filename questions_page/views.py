from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from .forms import ImageForm, QuestionForm
from .models import Image

# Create your views here.

def questionMain_view(request):
    return render(request, 'questions_page/questions_main.html')

@login_required
def postQ_view(request):
    if request.method == 'POST':
    
        questionForm = QuestionForm(request.POST, request.user)
        img_form = ImageForm(request.POST, request.FILES)

        if questionForm.is_valid() and img_form.is_valid():
            question_obj = questionForm.save(commit=False)
            question_obj.user = request.user
            question_obj.save()
            for img in request.FILES.getlist('images'):
                Image.objects.create(image=img, question=question_obj)
            return redirect('postQ_view')

    questionForm = QuestionForm()
    img_form = ImageForm(request.POST, request.FILES)
    return render(request, 'questions_page/postQ.html', {"questionForm":questionForm, "img_form": img_form})
