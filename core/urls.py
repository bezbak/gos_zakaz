from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('apps.news.urls')),
    path('gallery/', include('apps.gallery.urls')),
    path('team/', include('apps.team.urls')),
    path('', include('apps.pages.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    prefix_default_language=False
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
