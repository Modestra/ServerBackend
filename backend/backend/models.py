import uuid
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField(null=False, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=20, null=False, default=None)
    email = models.EmailField(null=False)
    userage = models.PositiveIntegerField(null=False, default=0)

    def __str__(self):
        return self.name
