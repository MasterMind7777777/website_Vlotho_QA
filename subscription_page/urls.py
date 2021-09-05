from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pay_with_robokassa, name='pay_with_robokassa'),
]