from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('password_change/', views.password_change_view, name='password_change_view'),
]