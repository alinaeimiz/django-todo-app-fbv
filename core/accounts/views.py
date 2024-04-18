from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    '''
    login function and it try to redirect users are login  to home page 
    '''
    if not request.user.is_authenticated:
        if request.method == 'POST':
           form = AuthenticationForm(request=request, data=request.POST)
           if form.is_valid():
               username = form.cleaned_data.get('username')
               password = form.cleaned_data.get('password')
               user = authenticate(request, username=username, password=password)
               if user is not None:
                   login(request, user)
                   return redirect('/')
        return render(request, 'login.html')
    else:
        return redirect('/')
    
    
@login_required    
def logout_view(request):
    '''
    logout for our app
    '''
    logout(request)
    return redirect('/')


def register_view(request):
    '''
    is a function for creating form to our app
    '''
    if not request.user.is_authenticated:
        if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/accounts/login')
        return render(request, 'register.html')
    return redirect('/')    
    