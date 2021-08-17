from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('registration', views.registration_view, name='registration_view'),
    path('', include('django.contrib.auth.urls')),
]