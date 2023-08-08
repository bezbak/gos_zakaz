from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Team, Struct, MainInfo,Tourism,Links

class MainInfoAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = MainInfo
        fields = ('text',)

class MainInfoAdmin(admin.ModelAdmin):
    form = MainInfoAdminForm

class TourismAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Tourism
        fields = ('text',)

class TourismAdmin(admin.ModelAdmin):
    form = TourismAdminForm

admin.site.register(Tourism, TourismAdmin)
admin.site.register(MainInfo, MainInfoAdmin)    
admin.site.register(Team,TranslationAdmin)
admin.site.register(Links)
admin.site.register(Struct,TranslationAdmin)