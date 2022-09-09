from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login ,logout
from .forms import UserRegisterForm, UserProfileForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
def user_register(request):
    # form = UserRegisterForm()    
    form_user = UserRegisterForm()
    form_profile = UserProfileForm()
    if request.method=="POST":
        form_user = UserRegisterForm(request.POST)
        form_profile = UserProfileForm(request.POST)#dosyaları almak için
        if form_user.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()

            login(request,user)
            
            # return redirect('home')
    context = {
        'register_form': form_user,
        'form_profile': form_profile,
    }
    return render(request, 'users/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, 'Login successfully')
            login(request, user)
            return redirect('blog-home')
    context = {
        'login_form' : form
    }
    return render(request, 'users/login.html', context)

def user_logout(request):
    messages.success(request, 'Logout successfully')
    logout(request)
    return redirect('blog-home')

@login_required
def user_profile(request):
     return render(request, 'users/profile.html')