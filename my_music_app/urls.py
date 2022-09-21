from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_music_app.web_app.urls')),
] + static(settings.MEDIA_URL, media_root=settings.MEDIA_ROOT)
