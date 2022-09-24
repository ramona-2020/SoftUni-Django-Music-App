from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from my_music_app.settings import LOGIN_REDIRECT_URL
from my_music_app.users.forms.users import CustomUserCreationForm


@login_required(login_url=LOGIN_REDIRECT_URL)
def dashboard(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'users/dashboard.html', context)


def register(request):
    form = CustomUserCreationForm(request.POST or None)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')

    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)
