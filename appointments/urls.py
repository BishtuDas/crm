from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    path('appointments/' ,views.appointments , name="appointments"),
    

]