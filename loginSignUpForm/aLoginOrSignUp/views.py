from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm    
from .forms import signUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash  #to redirect to a page after changing password. bcaus
#httpresponseredirect directly doesn't work here directly.

from django.shortcuts import  HttpResponseRedirect

# Create your views here.
#Singn Up Form :
def signUp(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=signUpForm(request.POST)
            if fm.is_valid():
                fm.save()
                fm=signUpForm() 
                messages.info(request,'Thanks!, Ur form has been submitted. ')
        else:
            fm=signUpForm()
        return render(request,'signUp.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


#Login Form :
def loginUp(request):
    if request.method=='POST':
        lgfm=AuthenticationForm(request=request,data=request.POST)
        if lgfm.is_valid():
            uName=lgfm.cleaned_data['username']
            uPassword=lgfm.cleaned_data['password']
            user=authenticate(username=uName,password=uPassword)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
    else:
        lgfm=AuthenticationForm()
    return render(request,'login.html',{'lgfm':lgfm})


#Showing Dashbord or HomePage after Logging
def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'userName':request.user})
    else:
        return HttpResponseRedirect('/login/')


# f(x) for Logout button
def UserLogout(request):
    logout(request)
    return HttpResponseRedirect('/')


#Changing User password, Old password needed to create new Password :
def changePass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password Changed Successfully !')
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'changePass.html',{'form':fm} )
    else:
        return HttpResponseRedirect('/login/')


#Change Password Without entering old Password :
def chngPassWEOldPass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,'Password Changed Successfully !')
                return HttpResponseRedirect('/profile/')
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,'chngPassWEOldPass.html',{'form':fm} )
    else:
        return HttpResponseRedirect('/chngPassWEOldPass/')