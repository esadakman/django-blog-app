from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login ,logout
from .forms import UserForm, UserProfileForm
from django.contrib import messages
def home(request):
    return render(request, 'templates/base.html')


def user_register(request):
    form = UserForm()   
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form)
            photo = form.cleaned_data['user_image']
            name = form.cleaned_data['name']
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password, name=name, photo=photo)
            messages.success(request, 'Registered successfully')
            return redirect('login')
        else :
            messages.error(request, "Registration failed")
            
    context = {
        'register_form' : form
    }
    return render(request, 'users/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, 'Login successfully')
            login(request, user)
            return redirect('home')
    context = {
        'login_form' : form
    }
    return render(request, 'users/login.html', context)

def user_logout(request):
    messages.success(request, 'Logout successfully')
    logout(request)
    return redirect('home')


