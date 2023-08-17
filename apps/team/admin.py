from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Team, Struct, MainInfo,Tourism,Links, Images,Corruption, GosLinks

class MainInfoAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    text_ru = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = MainInfo
        fields = ('text','text_ru')

class MainInfoAdmin(admin.ModelAdmin):
    form = MainInfoAdminForm

class TourismAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    text_ru = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Tourism
        fields = ('text','text_ru')

class TourismAdmin(admin.ModelAdmin):
    form = TourismAdminForm

class CorruptionAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    text_ru = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Corruption
        fields = ('text','text_ru')

class CorruptionAdmin(admin.ModelAdmin):
    form = CorruptionAdminForm
admin.site.register(Tourism, TourismAdmin)
admin.site.register(Corruption, CorruptionAdmin)
admin.site.register(MainInfo, MainInfoAdmin)    
admin.site.register(Team,TranslationAdmin)
admin.site.register(Links)
admin.site.register(Images)
admin.site.register(Struct,TranslationAdmin)
admin.site.register(GosLinks,TranslationAdmin)