import uuid
from django.db import models
from datetime import datetime
from backend.models import User as BaseUser

class Card(models.Model):
    """Карточка товара для магазина"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sell = models.DecimalField(max_digits=7, decimal_places=2)
    address = models.TextField()
    time = models.DateTimeField(default=datetime.now)

class User(BaseUser):
    """Пользователь для проекта SolarLab"""

    class Meta:
        abstract = True
class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    parentid = models.UUIDField(default=uuid.uuid4)

class Advert(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True