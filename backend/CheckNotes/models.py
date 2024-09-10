from django.db import models
from backend.models import User

class NoteList(models.Model):
    id = models.AutoField(primary_key=True)

