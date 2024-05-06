from django.urls import path
from . import views

app_name = 'business'
urlpatterns = [
    
    path("company-profile" , views.companyprofile, name="companyprofile"),
    path("doctor-profile" , views.doctorprofile, name="doctorprofile"),
    

]