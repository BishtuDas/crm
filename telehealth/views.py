from django.shortcuts import render

# Create your views here.

def telehealth(request):
    return render(request , 'telehealth.html')
