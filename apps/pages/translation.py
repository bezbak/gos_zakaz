from modeltranslation.translator import TranslationOptions,register
from .models import Rayons

@register(Rayons)
class RayonsTranslationOptions(TranslationOptions):
    fields = ('name',)