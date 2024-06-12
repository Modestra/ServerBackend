from django.db import models

class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name;