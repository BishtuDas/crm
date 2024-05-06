from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request , 'index.html')

def userprofile(request):
    return render(request , 'user_profile.html')