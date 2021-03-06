"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
import subscriptions

urlpatterns = [
    path('', include('home_page.urls')),
    path('robokassa/', include('robokassa.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('subscriptions/', include('subscriptions.urls')),
    path('subscription/', include('subscription_page.urls')),
    path('blog/', include('blog.urls')),
    path('authentication/', include('auth_page.urls')),
    path('profile/', include('profile_page.urls')),
    path('colourMix/', include('colourMix_page.urls')),
    path('questions/', include('questions_page.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)