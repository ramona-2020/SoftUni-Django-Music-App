from django.urls import path

from my_music_app.users.views import dashboard, register

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
]
