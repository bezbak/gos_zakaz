from modeltranslation.translator import register, TranslationOptions
from .models import Team, Struct, MainInfo, Tourism

@register(Team)
class TeamTranslationsOptions(TranslationOptions):
    fields = ('full_name','job_title')
    
@register(Struct)
class StructTranslationsOptions(TranslationOptions):
    fields = ('name',)

@register(MainInfo)
class MainInfoTranslationsOptions(TranslationOptions):
    fields = ('text',)

@register(Tourism)
class TourismTranslationsOptions(TranslationOptions):
    fields = ('text',)