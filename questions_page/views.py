from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .forms import ImageForm, QuestionForm
from .models import Image, Question

# Create your views here.
@user_passes_test(lambda u: u.groups.filter(name='Premium').count() > 0)
@login_required
def questionMain_view(request):
    return render(request, 'questions_page/questions_main.html')

@user_passes_test(lambda u: u.groups.filter(name='Premium').count() > 0)
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

def displayQ_view(request):

    questions = Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'questions_page/questions_list.html', {'questions' : questions})

def question_detail_view(request, pk):

    question = get_object_or_404(Question, pk=pk)
    images = Image.objects.filter(question=pk)
    return render(request, 'questions_page/question_detail.html', {'question': question, 'images': images})