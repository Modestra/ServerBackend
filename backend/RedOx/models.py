from django.db import models

class Notes(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = models.ImageField(max_length=30)