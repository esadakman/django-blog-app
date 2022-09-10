from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login ,logout
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# , UserProfileForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})   

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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user_profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)





















     
    # form_user = UserRegisterForm()
    # form_profile = UserProfileForm()
    # if request.method=="POST":
    #     form_user = UserRegisterForm(request.POST)
    #     form_profile = UserProfileForm(request.POST)#dosyaları almak için
    #     if form_user.is_valid():
    #         user = form_user.save()
    #         profile = form_profile.save(commit=False)
    #         profile.user = user
    #         profile.save()

    #         login(request,user)
            
    #         # return redirect('home')
    # context = {
    #     'register_form': form_user,
    #     'form_profile': form_profile,
    # }
    # return render(request, 'users/register.html', context)