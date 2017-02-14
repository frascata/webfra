from modeltranslation.translator import TranslationOptions
from .models import HomePage, OneSectionPage, Portfolio, ThreeSectionsPage, Project
from modeltranslation.translator import translator


class TranslatedHomePage(TranslationOptions):
    fields = ('main_content_title', 'main_content', 'portfolio_content_title',)


class TranslatedOneSectionPage(TranslationOptions):
    fields = ('content',)


class TranslatedThreeSectionsPage(TranslationOptions):
    fields = ('content', 'second_content', 'third_content',)


class TranslatedPortfolio(TranslationOptions):
    fields = ('title', 'content',)


class TranslatedProject(TranslationOptions):
    fields = ('name',)


translator.register(HomePage, TranslatedHomePage)
translator.register(OneSectionPage, TranslatedOneSectionPage)
translator.register(ThreeSectionsPage, TranslatedThreeSectionsPage)
translator.register(Portfolio, TranslatedPortfolio)
translator.register(Project, TranslatedProject)
