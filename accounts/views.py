from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required


# Create your views here.
def doctor_list(request):
    doctors = User.objects.all()
    context = {
        'doctorsHTML': doctors
    }
    return render(request,'user/doctor_list.html',context)



def doctor_details(request , slug):
    doctorDetails = Profile.objects.get(slug = slug)
    context = {
        'doctorDetails': doctorDetails
    }
    return render(request,'user/doctor_details.html',context)


# def user_login(request):
#     if request.method == 'POST':
#         form = Login_Form()
#         username = request.POST('username')
#         password = request.POST('password')
#         user = authenticate(request , username = username , password = password)
#         if user is not None:
#             login(request , user)
#     else:
#         form = Login_Form() 
#         return redirect('accounts:doctor_list')      
#     context = { 
#             'form': form  
#     }
#     return render(request,'user/user_login.html',context)
    
def user_login(request):
    if request.method == 'POST':
        form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('accounts:doctor_list')
        # else:
        #     messages.error(request, "كلمه السر غير صحيحه")
    else:
        form = Login_Form()

    return render(request , 'user/user_login.html' , {
        'form' : form,
        'title' : 'تسجيل الدخول'
    })


@login_required()
def myProfile(request):

    context = {

    }
    return render(request,'user/myprofile.html',context)


def updateProfile(request):
    userForm = UpdateUserForm(instance=request.user)
    profileForm = UpdateProfileForm(instance=request.user.profile)
    context = {
        'userForm' : userForm,
        'profileForm': profileForm
        }
    if request.method == 'POST':
        userForm = UpdateUserForm(request.POST , instance=request.user)
        profileForm = UpdateProfileForm(request.POST ,request.FILES ,instance=request.user.profile)

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            return redirect('accounts:doctor_list')
        
    return render(request,'user/update_profile.html',context)


def signUp(request):
    if request.method == 'POST':
        signupform = UserCreationForms(request.POST)
        context = {
        'signupform':signupform
        }
        if signupform.is_valid():
            signupform.save()
            username = signupform.cleaned_data.get('username')
            password = signupform.cleaned_data.get('password')
            user = authenticate(username='username', password='password')
            login(request , user)
            return redirect('accounts:doctor_list')
    else:
        signupform = UserCreationForms()
    return render(request , 'user/signup.html',{
        'signupform':signupform
        })