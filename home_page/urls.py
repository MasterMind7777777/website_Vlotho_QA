from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainHome_view, name='mainHome_view'),
]