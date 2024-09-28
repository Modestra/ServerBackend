import uuid
from django.db import models
from datetime import datetime, timedelta
from backend.models import User as BaseUser
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
import jwt

class User(models.Model):
    """Пользователь для проекта SolarLab"""
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField(default=uuid.uuid4)

    email = models.EmailField(db_index=True, unique=True)
    username = models.CharField(db_index=True, max_length=255, unique=True, blank=True)
    password = models.TextField(blank=True)

    isAdmin = models.BooleanField(default=False)

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
    
    def admin(self):
        return self.isAdmin
    
class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.UUIDField(default=uuid.uuid4,)
    name = models.CharField(max_length=255, blank=False, unique=True)
    parentid = models.UUIDField(blank=True)

class Advert(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField()
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    cost = models.PositiveBigIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    location = models.TextField()
    categoryid = models.UUIDField(blank=False)

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    image_id = models.UUIDField(blank=False)
    image = models.ImageField(upload_to='images/')

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField(blank=False)
    advert_id = models.UUIDField(blank=False)
    text = models.TextField()
