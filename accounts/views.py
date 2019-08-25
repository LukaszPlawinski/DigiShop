from django.shortcuts import render,redirect,reverse
from .forms import user_login_form
from django.contrib import auth

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