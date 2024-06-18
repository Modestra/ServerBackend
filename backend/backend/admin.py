from django.contrib import admin
from . import models

class CategoryPerson(admin.ModelAdmin):
    pass

admin.site.register(models.Person, CategoryPerson)



