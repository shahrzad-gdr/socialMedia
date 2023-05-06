from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index(request):
    return render(request,'account/index.html')


def user_register(request):
    return render(request, 'account/register.html')


def user_login(request):
    global user
    title = 'login'

    if request.method == 'POST':
        email= request.POST.get("email")
        password= request.POST.get("password")
        remember_me= request.POST.get("remember_me")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            print('user is {0}, {1}'.format(user, user.first_name))

            if user.is_active:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)  # Here if the remember me is False, that is why expiry is set to 0 seconds. So it will automatically close the session after the browser is closed.

                return redirect('index')
            else:
                messages.error(request, 'This account is not active', 'warning')
        else:
            messages.error(request, 'Invalid email or password', 'danger')



    context = {
        'title' : title,
    }
    return render(request, 'account/login.html', context)


@login_required()
def user_logout(request):
    logout(request)
    return redirect('login')