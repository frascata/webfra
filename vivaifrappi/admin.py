from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage, OneSectionPage, Slide, Portfolio, ThreeSectionsPage, Project


# Register your models here.
admin.site.register(HomePage, PageAdmin)
admin.site.register(OneSectionPage, PageAdmin)
admin.site.register(ThreeSectionsPage, PageAdmin)
admin.site.register(Slide)
admin.site.register(Portfolio)
admin.site.register(Project)
