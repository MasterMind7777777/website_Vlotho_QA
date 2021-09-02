from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .forms import ImageForm, QuestionForm, AnswerForm, MediaFileForm
from .models import Image, Question, Answer, MediaFile

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
            return redirect('question_detail_view', pk=question_obj.pk)

    questionForm = QuestionForm()
    img_form = ImageForm(request.POST, request.FILES)
    return render(request, 'questions_page/postQ.html', {"questionForm":questionForm, "img_form": img_form})

def displayQ_view(request):

    questions = Question.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'questions_page/questions_list.html', {'questions' : questions})

def question_detail_view(request, pk):

    question = get_object_or_404(Question, pk=pk)
    can_edit = False
    if request.user == question.user:
        can_edit = True
    images = Image.objects.filter(question=pk)

    answer = None
    media_files = None
    print('question.answered: ', question.answered)
    if question.answered:
        answer = get_object_or_404(Answer, question=question)
        media_files = MediaFile.objects.filter(answer=answer)
    
    
    return render(request, 'questions_page/question_detail.html', {'question': question, 'images': images, 'can_edit': can_edit, 'answer': answer, 'media_files': media_files})

def question_edit_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        img_form = ImageForm(request.POST, request.FILES)
        print('form: ', form.is_valid(), 'imgform: ', img_form.is_valid())
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.published_date = timezone.now()
            question.save()
            for img in request.FILES.getlist('images'):
                Image.objects.create(image=img, question=question)
            return redirect('question_detail_view', pk=question.pk)
    else:
        form = QuestionForm(instance=question)
        img_form = ImageForm(request.POST, request.FILES)
    return render(request, 'questions_page/question_edit.html', {'form': form, 'img_form': img_form})

@user_passes_test(lambda u: u.groups.filter(name='Master').count() > 0)
@login_required
def questions_answers_view(request):

    questions = Question.objects.filter(published_date__lte=timezone.now(), answered__exact=False).order_by('published_date')
    return render(request, 'questions_page/questions_answer.html', {'questions' : questions})

@user_passes_test(lambda u: u.groups.filter(name='Master').count() > 0)
@login_required
def question_answer_view(request, pk):

    question = get_object_or_404(Question, pk=pk)
    can_edit = False
    if request.user == question.user:
        can_edit = True
    
    images = Image.objects.filter(question=pk)

    if request.method == 'POST':
        answer_form = AnswerForm(request.POST, request.user)
        media_form = MediaFileForm(request.POST, request.FILES)

        if answer_form.is_valid() and media_form.is_valid():
            answer_obj = answer_form.save(commit=False)
            answer_obj.user = request.user
            answer_obj.question = question
            answer_obj.save()
            for media in request.FILES.getlist('media_files'):
                MediaFile.objects.create(media_file=media, answer=answer_obj)
            
            question.answered = True
            question.save()
            return redirect('question_detail_view', pk=question.pk)


    answer_form = AnswerForm()
    media_form = MediaFileForm(request.POST, request.FILES)

    return render(request, 'questions_page/question_answer.html', {'question': question, 'images': images, 'can_edit': can_edit, 'answer_form': answer_form, 'media_form': media_form})