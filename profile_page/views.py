from django.shortcuts import render

# Create your views here.
def profile_view(request):
    return render(request, 'profile_page/profile_main.html')