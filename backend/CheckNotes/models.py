from django.db import models
from backend.models import User

class NoteList(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
