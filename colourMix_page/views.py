from django.shortcuts import render

#Create your views here.
def colourMixMain_view(request):
    return render(request, 'colourMix_page/colourMix_main.html')