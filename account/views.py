from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def reset(request):
    return render(request, 'reset_password.html')

def forgot(request):
    return render(request , 'forgot_password.html')