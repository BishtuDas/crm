from django.urls import path
from . import views

app_name = 'business'
urlpatterns = [
    
    path("company_profile/" , views.company_profile, name="company_profile"),
    path("doctor_profile/" , views.doctor_profile, name="doctor_profile"),
    path("my_team/" , views.my_team, name="my_team"),
    path("reports/" , views.reports, name="reports"),
    path("my_locations/" , views.my_locations, name="my_locations"),




   


  
    

]