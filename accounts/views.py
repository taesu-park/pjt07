from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm

# Create your views here.

def index(request):
    User = get_user_model()
    Users = User.objects.all() # 404 쓰면 왜안됩니까? => pk 없음
    context = {
        'users' : Users
    }
    return render(request, 'accounts/index.html', context)
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def profile(request, account_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=account_pk)
    context = {
        'user_profile' : user
    }
    return render(request, 'accounts/profile.html', context)