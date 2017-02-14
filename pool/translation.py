from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import translator

from .models import PoolPage


class TranslatedPoolPage(TranslationOptions):
    fields = ('content',)


translator.register(PoolPage, TranslatedPoolPage)
