from django.contrib import admin
from django import forms
from multiupload.fields import MultiFileField
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from apps.news.models import News, Media
from django.utils.translation import gettext_lazy as _
# Register your models here.
class NewsAdminForm(forms.ModelForm, forms.Form):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    description_ru = forms.CharField(widget=CKEditorUploadingWidget())
    images = MultiFileField()

    class Meta:
        model = News
        fields = "__all__"

class NewsAdmin(TranslationAdmin):
    form = NewsAdminForm
    def save_model(self, request, obj, form, change):
        obj2 = News.objects.get(id=obj.id)
        print(obj2)
        for each in form.cleaned_data['images']:
            Media.objects.create(news=obj2, image=each)
        super().save_model(request, obj, form, change)
    
admin.site.register(News, NewsAdmin)
admin.site.register(Media)