from django.urls import path
from . import views
app_name='clients'
urlpatterns = [
    path('clients_all/', views.clients_all, name='clients_all'),
    path('add_clients/', views.add_clients, name='add_clients'),



    
]