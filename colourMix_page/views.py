from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .forms import ColourForm
from .hexToCmy import Convert
from .models import ColourCatalog
from django.contrib.auth.decorators import login_required, user_passes_test
from math import sqrt

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

def closest_color(rgb, colours):
    r, g, b = rgb
    color_diffs = []
    for color in colours:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Premium').count() > 0)
def colour_mix_pigment_view(request):

    if request.method == "POST":
        form = ColourForm(request.POST)
        if form.is_valid():
            hex = form['colour'].value()
            vol = form['volume'].value()
            vol = int(vol)

            rgb = Convert.hex_to_rgb(hex)
            available_colors_obj = ColourCatalog.objects.all().filter(hex__startswith="#")
            available_colors = []

            for colour in available_colors_obj:
                available_colors.append(Convert.hex_to_rgb(colour.hex))
            
            clos_col = closest_color(rgb, available_colors)
            clos_col_hex = Convert.rgb_to_hex(clos_col)
            try:
                color_obj = ColourCatalog.objects.get(hex=clos_col_hex)
            except ObjectDoesNotExist:
                clos_col_hex = clos_col_hex.upper()
                color_obj = ColourCatalog.objects.get(hex=clos_col_hex)
            

            col1 = color_obj.colour1
            col2 = color_obj.colour2
            col3 = color_obj.colour3
            col4 = color_obj.colour4

            col1g = color_obj.colour1_grams/1000
            col2g = color_obj.colour2_grams/1000
            col3g = color_obj.colour3_grams/1000
            col4g = color_obj.colour4_grams/1000

            full_mass = col1g + col2g + col3g + col4g + vol
            prosentageCol = vol / full_mass

            col0g = 0
            col1g = round((col1g * prosentageCol * vol),2)
            col2g = round((col2g * prosentageCol * vol),2)
            col3g = round((col3g * prosentageCol * vol),2)
            col4g = round((col4g * prosentageCol * vol),2)

            fin_mass = col1g + col2g + col3g + col4g
            base_mass = round((vol - fin_mass),2)

            if col1 == 'K':
                col0g = col1g
                col1 = col2
                col2 = col3
                col3 = col4
                col4 = '-'

                col1g = col2g
                col2g = col3g
                col3g = col4g
                col4g = 0
            elif col2 == 'K':
                col0g = col2g
                col2 = col3
                col3 = col4
                col4 = '-'

                col2g = col3g
                col3g = col4g
                col4g = 0
            elif col3 == 'K':
                col0g = col3g
                col3 = col4
                col4 = '-'

                col4g = 0
                col3g = col4g
            elif col4 == 'K':
                col0g = col4g
                col4 = '-'
                col4g = 0





            if color_obj.base_type == 'WHITE BASE (20,0% TiO2)':
                col5g = (base_mass / 100) * 20 + col0g
                base_mass = round((base_mass - col5g),2)
            else:
                col5g = col0g
                    

            return render(request, 'colourMix_page/colourMix_pigment.html', 
                {'form': form, 'base_mass': base_mass,
                'col1': col1, 'col2': col2, 'col3': col3, 'col4': col4, 
                'col1g': col1g, 'col2g': col2g, 'col3g': col3g, 'col4g': col4g, 'col5g': col5g})

    else:
        form = ColourForm()
    return render(request, 'colourMix_page/colourMix_pigment.html', {'form': form})

def fin_view(request):
    return render(request, 'colourMix_page/fin.html')