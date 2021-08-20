from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class MyPasswordChangeForm(PasswordChangeForm):
    frm = forms.ValidationError("old password was not correct!")
