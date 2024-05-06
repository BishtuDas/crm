from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/',views.signup , name='signup'),
    
    path('bye-bye/',views.byebye , name='byebye'),
    path('reset-password/' , views.reset , name='reset'),
    path('forgot-password/' ,views.forgot , name="forgot"),
]