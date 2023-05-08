from django.urls import path
from .views import *
from . import views
app_name = 'accounts'
urlpatterns = [
    path('doctor/',views.doctor_list,name='doctor_list'),
    path('login',views.user_login,name='user_login'),
    path('signup',views.signUp,name='signUp'),
    path('doctor/myprofile',views.myProfile,name='myProfile'),
    path('doctor/updateProfile',views.updateProfile,name='updateProfile'),
    path('doctor/<slug:slug>/',views.doctor_details,name='doctor_details'),
]
