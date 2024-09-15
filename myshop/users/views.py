from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username','')
            # TODO create user
            redirect('login/')
            messages.success(request, f'Регистрация {username} прошла успешно')
        else:
            messages.warning(request, f'Не получилось')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


    

