from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'account'
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/',views.signup , name='signup'),
    path('reset-password/' , views.reset , name='reset'),
    path('forgot-password/' ,views.forgot , name="forgot"),
    

]