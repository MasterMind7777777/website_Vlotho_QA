from django.shortcuts import render
from .forms import MyPasswordChangeForm


# Create your views here.
def profile_view(request):
    return render(request, 'profile_page/profile_main.html')

def password_change_view(request):
    form = MyPasswordChangeForm(user=request.user)
    errorMsg = False
    args = {'form': form, 'errorMsg' : errorMsg}
    if request.method == "POST":
        form = MyPasswordChangeForm(data=request.POST, user=request.user)
        print ("pooooooooooooost")
        print(form.is_valid())
        if form.is_valid():
            print ("valid") 
            form.save()
            return render(request, 'profile_page/profile_main.html', args)
        elif form.is_valid() == False:
            #raise MyPasswordChangeForm.frm
            print ("valid") 
            args['errorMsg'] = True
            return render(request, 'profile_page/password_change.html', args)

    return render(request, 'profile_page/password_change.html', args)