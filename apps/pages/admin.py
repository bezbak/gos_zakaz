from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from apps.pages.models import Police, DevFund, StateSymbols
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
