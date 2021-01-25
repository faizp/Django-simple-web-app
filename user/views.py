from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.http import JsonResponse
from django.contrib.auth.models import User


def home(request):
    if not request.user.is_authenticated:
        return redirect(my_view)
    else:
        # user = User.objects.get('username')
        return render(request, 'user/home.html')


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            form = UserRegisterForm()

        return render(request, 'user/register.html', {"form": form})
    else:
        return redirect(home)


def my_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username', False)
            password = request.POST.get('password', False)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse('true', safe=False)
            else:
                return JsonResponse('false', safe=False)
        else:
            return render(request, 'user/login.html')

    else:
        return redirect(home)



def logout_view(request):
    logout(request)
    return redirect(my_view)