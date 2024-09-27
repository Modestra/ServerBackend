import uuid
from django.db import models
from datetime import datetime, timedelta
from backend.models import User as BaseUser
from django.conf import settings
import jwt

class Card(models.Model):
    """Карточка товара для магазина"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sell = models.DecimalField(max_digits=7, decimal_places=2)
    address = models.TextField()
    time = models.DateTimeField(default=datetime.now)

class User(models.Model):
    """Пользователь для проекта SolarLab"""
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField(default=uuid.uuid4)

    email = models.EmailField(db_index=True, unique=True)
    username = models.CharField(db_index=True, max_length=255, unique=True, blank=True)
    password = models.TextField(blank=True)

    @property
    def token(self):
        """Получение JWT токена путем вызова user.token"""
        return self._generate_jwt_token()
    
    def _generate_jwt_token(self):

        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': 10000
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
    
class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    parentid = models.UUIDField(default=uuid.uuid4)

class Advert(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
