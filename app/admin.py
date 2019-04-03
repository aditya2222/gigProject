from django.contrib import admin
from .models import PagesModel, IndexModel

# Register your models here.

admin.site.register(PagesModel)
admin.site.register(IndexModel)
