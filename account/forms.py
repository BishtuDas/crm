# forms.py
from django import forms
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username","password1", "password2"]

    def _init_(self, *args, **kwargs):
            super(RegisterForm, self)._init_(*args, **kwargs)
            self.fields['username'].widget.attrs = {'class': 'form-control', 'placeholder':'Username without spaces', 'onkeyup':'userCheck()'}
           
            self.fields['password1'].widget.attrs = {'class': ' form-control' }
            self.fields['password2'].widget.attrs = {'class': ' form-control', 'onkeyup': 'pwfun()' }
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name"]
    def _init_(self, *args, **kwargs):
        super(ProfileForm, self)._init_(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control'}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput(),
    }