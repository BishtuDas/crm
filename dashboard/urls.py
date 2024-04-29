from django.urls import path
from . import views
app_name='dashboard'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user-profile/', views.userprofile , name='userprofile')
    # path('signup/',views.signup , name='signup'),
    # path('reset/' , views.reset , name='reset'),
    # path('forgot-password/' ,views.forgot , name="forgot"),
]