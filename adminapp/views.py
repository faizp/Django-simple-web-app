from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from user.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def user_details(request):
    if request.session.has_key('password'):
        users = User.objects.all()
        return render(request, 'admin/adminhome.html', {'users':users})
    else:
        return redirect(admin_login)


def delete_user(request, username):
    user = User.objects.get(username = username)
    user.delete()
    return redirect(user_details)

def admin_login(request):
    if request.session.has_key('password'):
        return redirect(user_details)
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username == 'admin' and password == 'admin':
                request.session['password'] = password
                return JsonResponse('true', safe=False)
            else:
                return JsonResponse('false', safe = False)
        else:
            return render(request, 'admin/admin_login.html')


def admin_logout(request):
    if request.session.has_key('password'):
        request.session.flush()
        return redirect(admin_login)
    else:
        return redirect(admin_login)


# def user_register(request):
#     if request.method == 'POST':
#         forms = UserRegisterForm(request.POST)
#         if forms.is_valid():
#             forms.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('login')
#     else:
#         forms = UserRegisterForm()
#     return render(request, 'admin/register.html', {"form": forms})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect(user_details)
    else:
        form = UserRegisterForm()
    return render(request, 'admin/register.html', {"form": form})


def edit(request, username):

    if request.session.has_key('password'):
        if request.method == 'POST':
            print(request.POST.get('email'))
            user = User.objects.get(username = username)
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.save()
            return redirect(user_details)
        else:
            user = User.objects.get(username = username)
            return render(request, 'admin/edit.html', {'user': user})
    else:
        return redirect(admin_login)


def admin_logout(request):
    if request.session.has_key('password'):
        request.session.flush()
        return redirect(admin_login)

#
# def user_search(request):
#     if request.session.has_key('password'):
#         if request.method == 'POST':
#             user_name = request.POST['searchbar']
#             user = User.objects.filter(username = user_name)
#             return render(request, 'admin/adminhome.html', {'user': user})
#     else:
#         return redirect(user_details)

