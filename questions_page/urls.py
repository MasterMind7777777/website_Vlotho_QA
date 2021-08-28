from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.questionMain_view, name='questionMain_view'),
    path('postQ/', views.postQ_view, name='postQ_view'),
]