from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import PoolPage


# Register your models here.
admin.site.register(PoolPage, PageAdmin)
