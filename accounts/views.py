from django.shortcuts import render,redirect,reverse
from .forms import user_login_form, register_user_form
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    login_form = user_login_form()
    return render(request, 'index.html')
    
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = user_login_form(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = user_login_form()
    return render(request, 'login.html', {'login_form': login_form})
    
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')
    
def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        registration_form = register_user_form(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
    else:
        registration_form = register_user_form()
    return render(request, 'registration.html', {
        "registration_form": registration_form})