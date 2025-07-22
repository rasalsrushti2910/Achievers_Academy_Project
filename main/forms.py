from django import forms
from .models import Admission
from .models import AdminUser


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['name', 'phone', 'email', 'course', 'city', 'pincode']



class AdminLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")




