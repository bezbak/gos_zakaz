from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from apps.news.models import News, Media
from django.utils.translation import gettext_lazy as _
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

class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    description_ru = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = "__all__"

class NewsAdmin(TranslationAdmin):
    form = NewsAdminForm
    inlines = [
        MediaInline,
    ]
admin.site.register(News, NewsAdmin)
admin.site.register(Media)