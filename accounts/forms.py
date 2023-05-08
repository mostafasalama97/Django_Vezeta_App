from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserCreationForms(UserCreationForm):
    username    = forms.CharField(label = 'الإسم' )
    email       = forms.EmailField(label = 'البريد الالكترونى' )
    first_name  = forms.CharField(label = 'الإسم الاخير' )
    last_name   = forms.CharField(label = 'الإسم الاول' )
    password1   = forms.CharField(label='كلمه السر', widget=forms.PasswordInput() , min_length=8)
    password2   = forms.CharField(label='تأكيد كلمه السر ', widget=forms.PasswordInput() , min_length=8)

    class Meta:
        model   = User
        fields  = ( 'username' ,'first_name' , 'last_name' , 'email' , 'password1' , 'password2' )
 


class Login_Form(forms.ModelForm):
    username = forms.CharField(max_length=80, label="الإسم")
    password = forms.CharField(label="كلمة المرور " , widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = '__all__' 


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label='الاسم الاول ')
    last_name = forms.CharField(label='الاسم الاخير ')
    email = forms.EmailField(label= 'البريد الاليكترونى ')
    class Meta:
        model   = User
        fields  = ('first_name' , 'last_name' , 'email')



class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model   = Profile
        fields  = ('who_i','name' ,'surname',
                    'subtitle','address','address_detail',
                    'price','number_phone','working_hours',
                    'Waiting_time', 'facebook', 'twitter',
                    'google', 'doctor','img',  'Specialist_doctor')