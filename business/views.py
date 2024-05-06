from django.shortcuts import render

# Create your views here.

def companyprofile(request):
    return render(request , 'user_profile.html')



def doctorprofile(request):
     return render(request , 'doctor_profile.html')

