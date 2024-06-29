from django.contrib import admin
from . import models

class CategoryUser(admin.ModelAdmin):
    pass

admin.site.register(models.User, CategoryUser)



