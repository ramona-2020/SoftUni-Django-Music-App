from django.urls import path

from my_music_app.web_app.views import homepage, add_album, album_details, edit_album, delete_album, profile_details, \
    delete_profile

urlpatterns = [
    path('', homepage, name='homepage'),
    path('album/add/', add_album, name='add_album'),
    path('album/details/<int:pk>/', album_details, name='album_details'),
    path('album/edit/<int:pk>/', edit_album, name='edit_album'),
    path('album/delete/<int:pk>/', delete_album, name='delete_album'),

    path('profile/details/', profile_details, name='profile_details'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]