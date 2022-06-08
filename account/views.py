from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import User


def RegistrationView(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.instance.set_password(form.cleaned_data.get('password'))
            form.save()

            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz")

            return redirect('account:login')

    return render(request, 'account/registration.html', {
        'form': form
    })

def LoginView(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)

                return redirect('main:index')

            form.add_error('password', "Login va/yoki parol noto'g'ri")

    return render(request, 'account/login.html', {
        'form': form
    })



def LogautView(request):
    logout(request)

    return redirect('main:index')

