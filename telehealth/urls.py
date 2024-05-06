from django.urls import path
from . import views
app_name='telehealth'
urlpatterns = [
    path('telehealth/', views.telehealth, name='telehealth'),
]