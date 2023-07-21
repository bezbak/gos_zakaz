from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.news.urls')),
    path('gallery/', include('apps.gallery.urls')),
    path('team/', include('apps.team.urls')),
]
