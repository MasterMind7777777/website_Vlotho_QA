from django.urls import path
from . import views

urlpatterns = [
    path('', views.colourMixMain_view, name='colourMixMain_view'),
    path('fin/', views.fin_view, name='fin_view'),
    ]