from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login
from .forms import UserForm, UserProfileForm
def home(request):
    return render(request, 'templates/base.html')

def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        # if user:
        #     messages.success(request, 'Login successfully')
        #     login(request, user)
        return redirect('home')
    context = {
        'login_form' : form
    }
    return render(request, 'users/login.html', context)