from django.contrib import admin
from django import forms
from apps.news.models import News, Media
# Register your models here.
class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = (
            'image',
            'news'
        )
class MediaInline(admin.TabularInline):
    form = MediaForm
    model = Media
    extra = 2
    
class NewsAdmin(admin.ModelAdmin):
    inlines = [
        MediaInline,
    ]


admin.site.register(News, NewsAdmin)
admin.site.register(Media)