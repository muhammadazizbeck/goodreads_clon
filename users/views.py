from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from .forms import UserCreateForm,ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RegisterView(View):
    def get(self,request):
        create_form = UserCreateForm()
        context = {
            'form':create_form
        }
        return render(request,'users/register.html',context)
    

    def post(self,request):
        create_form = UserCreateForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form':create_form
            }
            return render(request,'users/register.html',context)
    
class LoginView(View):
    def get(self,request):
        login_form = AuthenticationForm()
        context = {
            'form':login_form
        }
        return render(request,'users/login.html',context)
    
    def post(self,request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request,user)
            messages.success(request,'You have successfully logged in.')
            return redirect('books:list')
        context = {
            'form':login_form
        }
        return render(request,'users/login.html',context)
    
class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        context = {
            'user':request.user
        }
        return render(request,'users/profile.html',context)
    

class LogoutView(LoginRequiredMixin,View):
    def post(self,request):
        logout(request)
        messages.info(request,'You have successfully logged out.')
        return redirect('landing_page')
    

class ProfileUpdateView(LoginRequiredMixin,View):
    def get(self,request):
        profile_update_form = ProfileUpdateForm(instance=request.user)
        context = {
            'form':profile_update_form
        }
        return render(request,'users/profile_update.html',context=context)

    def post(self,request):
        profile_update_form = ProfileUpdateForm(instance=request.user,data=request.POST,files=request.FILES)
        if profile_update_form.is_valid():
            profile_update_form.save()
            messages.success(request,'You have successfully updated your profile informations')
            return redirect('users:profile')
        else:
            context = {
                'form':profile_update_form
            }
            return render(request,'users/profile_update.html',context=context)
