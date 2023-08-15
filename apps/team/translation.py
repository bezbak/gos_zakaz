from modeltranslation.translator import register, TranslationOptions
from .models import Team, Struct,GosLinks

@register(Team)
class TeamTranslationsOptions(TranslationOptions):
    fields = ('full_name','job_title')
    
@register(Struct)
class StructTranslationsOptions(TranslationOptions):
    fields = ('name','description',)
@register(GosLinks)
class GosLinksTranslationsOptions(TranslationOptions):
    fields = ('name',)
