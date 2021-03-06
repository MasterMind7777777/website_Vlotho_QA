from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.questionMain_view, name='questionMain_view'),
    path('postQ/', views.postQ_view, name='postQ_view'),
    path('all/', views.displayQ_view, name='displayQ_view'),
    path('question/<int:pk>/', views.question_detail_view, name='question_detail_view'),
    path('question/<int:pk>/edit/', views.question_edit_view, name='question_edit_view'),
    path('question/<int:pk>/answer/', views.question_answer_view, name='question_answer_view'),
    path('answer/', views.questions_answers_view, name='questions_answers_view'),
]
