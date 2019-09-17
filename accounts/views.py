from django.shortcuts import render,redirect,reverse
from .forms import user_login_form, register_user_form, UserEditForm
from django.contrib import auth
from django.contrib.auth.models import User
from shop.views import product_list
from shop.models import Category
from django.contrib.auth.decorators import login_required

# Importing coategories list which is used in Nav
categories = Category.objects.all()

''' When user is logged in redirect him to login page,
if method is Post and login form valid then login'''
def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('shop:product_list'))
    if request.method == "POST":
        login_form = user_login_form(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('shop:product_list'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = user_login_form()
    return render(request, 'login.html', {'login_form': login_form, 'categories':categories})
    
    
'''Logout function'''
@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('shop:product_list'))
    
    
'''Registration Function'''
def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('shop:product_list'))
        
    if request.method == "POST":
        registration_form = register_user_form(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
                                     
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('shop:product_list'))
                
    else:
        registration_form = register_user_form()
    return render(request, 'registration.html', {
        "registration_form": registration_form, 'categories':categories})
        
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
    
        if user_form.is_valid() :
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request,
        'edit.html',
        {'user_form': user_form})