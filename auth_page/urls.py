from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.auth_view, name='auth_view'),
    path('registration', views.registration_view, name='registration_view'),
    path('', include('django.contrib.auth.urls')),
]