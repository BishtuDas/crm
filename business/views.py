from django.shortcuts import render

# Create your views here.

def company_profile(request):
    return render(request , 'company_profile.html')



def doctor_profile(request):
     return render(request , 'doctor_profile.html')



def  my_team(request):
     return render(request , 'my_team.html')



def   reports(request):
     return render(request , 'reports.html')




def my_locations(request):
     return render(request , 'my_locations.html')

















 