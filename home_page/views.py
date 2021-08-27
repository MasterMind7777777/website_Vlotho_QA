from django.shortcuts import render

# Create your views here.
def mainHome_view(request):
    return render(request, 'home_page/main_home.html')