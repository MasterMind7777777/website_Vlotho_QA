from django.shortcuts import render
from .forms import registrationForm

def auth_view(request):
    return render(request, 'auth_page/auth_main.html')

def registration_view(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()


            return render(request, 'auth_page/auth_main.html')
    else:
        form = registrationForm()
    return render(request, 'auth_page/registration.html', {'form': form})
