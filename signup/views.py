from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import auth
# Create your views here.

def home(request):
    return render(request, 'registration/base.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('registration:welcome')
        else:
            messages.info("Credentials not valid")
            return redirect(request, 'registration/login.html')
    else:
        form = LoginForm()
        
    return render(request, 'registration/login.html', {'form':form})


def logout(request):
    auth.logout(request)
    return redirect("/")