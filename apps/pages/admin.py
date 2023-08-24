from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from apps.pages.models import Police, DevFund, StateSymbols, Rayons
# Register your models here.
class PoliceAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    text_ru = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Police
        fields = ('text', 'text_ru')
@admin.register(Police)
class PoliceAdmin(admin.ModelAdmin):
    form = PoliceAdminForm

class DevFundAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    text_ru = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = DevFund
        fields = ('text', 'text_ru')
        
@admin.register(DevFund)
class DevFundAdmin(admin.ModelAdmin):
    form = DevFundAdminForm

class StateSymbolsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    text_ru = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = StateSymbols
        fields = ('text', 'text_ru')

@admin.register(StateSymbols)
class StateSymbolsAdmin(admin.ModelAdmin):
    form = StateSymbolsAdminForm

class RayonsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    text_ru = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Rayons
        fields = "__all__"

class RayonsAdmin(TranslationAdmin):
    form = RayonsAdminForm
admin.site.register(Rayons, RayonsAdmin)