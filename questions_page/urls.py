from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionMain_view, name='questionMain_view'),
    path('postQ/', views.postQ_view, name='postQ_view'),
    path('all/', views.displayQ_view, name='displayQ_view'),
    path('question/<int:pk>/', views.question_detail_view, name='question_detail_view'),
]
