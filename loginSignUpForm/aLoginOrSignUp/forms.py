from cProfile import label
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class signUpForm(UserCreationForm):
    password2=forms.CharField(          #adding our own field. By default it shows only username and password.
        label='Password (again)'
        ,widget=forms.PasswordInput()
    )
    class Meta:
        model=User
        fields=['username','first_name','last_name','email'] #these fields spellings are pre-defined.
        labels={'email':'Email'}    