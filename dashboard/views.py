from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request , 'index.html')

def userprofile(request):
    return render(request , 'user_profile.html')