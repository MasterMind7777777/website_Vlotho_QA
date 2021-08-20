from django.shortcuts import render , redirect
from .forms import ColourForm
from .hexToCmyk import Convert
from django.contrib.auth.decorators import login_required

#Create your views here.
@login_required
def colourMixMain_view(request):
    if request.method == "POST":
        form = ColourForm(request.POST)
        if form.is_valid():
            hex = form['colour'].value()
            vol = form['volume'].value()
            vol = int(vol)
            cmyk = Convert.rgb_to_cmyk(Convert.hex_to_rgb(hex)) 
            print(cmyk)
            c = cmyk[0]
            m = cmyk[1]
            y = cmyk[2]
            k = cmyk[3]
            coef = (vol / 400)
            c = c * coef
            m = m * coef
            y = y * coef
            k = k * coef

            c = round(c, 2)
            m = round(m, 2)
            y = round(y, 2)
            k = round(k, 2)
            water = vol - c - m - y - k


            return render(request, 'colourMix_page/colourMix_main.html', {'form': form, 'c': c, 'm':m, 'y': y, 'k': k, 'water': water})


            
    else:
        form = ColourForm()
    return render(request, 'colourMix_page/colourMix_main.html', {'form': form})

def fin_view(request):
    return render(request, 'colourMix_page/fin.html')