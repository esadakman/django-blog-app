from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login ,logout
from .forms import UserRegisterForm, UserProfileForm
from django.contrib import messages
def home(request):
    return render(request, 'templates/base.html')


def user_register(request):
    form = UserRegisterForm()   
    # if request.method == 'POST':
        # form = UserRegisterForm(request.POST, request.FILES)
        # if form.is_valid():
            # form.save() 
            # name = form.cleaned_data['name']
            # username = form.cleaned_data['username']
            # photo = form.cleaned_data['user_image']
            # password = form.cleaned_data['password1']
            # user = authenticate(username=username, password=password, name=name, photo=photo)
            # messages.success(request, 'Registered successfully')
            # return redirect('login')
        # else :
            # messages.error(request, "Registration failed") 
    # context = {
    #     'register_form' : form
    # }
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
            
            return redirect('home')
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
            return redirect('home')
    context = {
        'login_form' : form
    }
    return render(request, 'users/login.html', context)

def user_logout(request):
    messages.success(request, 'Logout successfully')
    logout(request)
    return redirect('home')


