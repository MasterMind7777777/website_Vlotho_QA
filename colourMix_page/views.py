from django.shortcuts import render
from .forms import ColourForm
from .hexToCmy import Convert
from django.contrib.auth.decorators import login_required, user_passes_test

#Create your views here.
@login_required
@user_passes_test(lambda u: u.groups.filter(name='Premium').count() > 0)
def colourMixMain_view(request):
    if request.method == "POST":
        form = ColourForm(request.POST)
        if form.is_valid():
            hex = form['colour'].value()
            vol = form['volume'].value()
            vol = int(vol)
            cmy = Convert.rgb_to_cmy(Convert.hex_to_rgb(hex)) 
            print(cmy)
            c = cmy[0]
            m = cmy[1]
            y = cmy[2]

            cmy_arr = [c,m,y]
            matches = [x for x in cmy_arr if x != 0]
            water = len(matches)*100 - sum(cmy_arr)
            coef = (vol / (len(matches)*100))    
            c = c * coef
            m = m * coef
            y = y * coef
            water = water * coef
            min_cmyk = min(c,m,y)
            if c == min_cmyk:
                k = c
                c = 0
            if m == min_cmyk:
                k = m
                m = 0
            if y == min_cmyk:
                k = y
                y = 0
            c = round(c, 2)
            m = round(m, 2)
            y = round(y, 2)
            k = round(k, 2)
            water = round(water, 2)


            return render(request, 'colourMix_page/colourMix_main.html', {'form': form, 'c': c, 'm':m, 'y': y, 'k': k, 'water': water})


            
    else:
        form = ColourForm()
    return render(request, 'colourMix_page/colourMix_main.html', {'form': form})

def fin_view(request):
    return render(request, 'colourMix_page/fin.html')