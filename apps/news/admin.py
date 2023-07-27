from django.contrib import admin
from apps.news.models import News, Media
# Register your models here.
admin.site.register(News)
admin.site.register(Media)