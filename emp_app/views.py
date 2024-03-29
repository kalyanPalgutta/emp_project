from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import *
from .models import *



def home(request):
    details = Details.objects.all()

    context = {

        'details': details,

    }
    return render(request, 'home.html', context)


def addDetails(request):
    if request.user.is_authenticated:
        form = addDetailsform()
        if (request.method == 'POST'):
            form = addDetailsform(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'addDetails.html', context)
    else:
        return redirect('home')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')