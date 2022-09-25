import time

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from my_music_app.web_app.forms.album_forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from my_music_app.web_app.forms.profile_forms import CreateProfileForm, DeleteProfileForm
from my_music_app.web_app.models import Profile, Album


def get_profile():
    return Profile.objects.first()


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def homepage(request):
    profile = get_profile()
    if not profile:
        return create_profile(request)

    albums = Album.objects.all()
    context = {
        'not_has_profile': True,
        'albums': albums
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your album was been created!')
            # return redirect('homepage')
        else:
            messages.error(request, 'Error saving form')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    contex = {
        'album': album
    }
    return render(request, 'album-details.html', contex)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album
    }
    return render(request, 'delete-album.html', context)


@login_required
def profile_details(request):
    profile = get_profile()
    current_user = request.user

    albums_count = Album.objects.count()
    context = {
        'albums_count': albums_count
    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = DeleteProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
