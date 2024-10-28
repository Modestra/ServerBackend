import uuid
from django.db import models
from datetime import datetime, timedelta
from backend.models import User as BaseUser
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
import jwt

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.UUIDField(default=uuid.uuid4,)
    name = models.CharField(max_length=255, blank=False, unique=True)
    parentid = models.UUIDField(blank=True)

class Advert(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField()
    advert_id = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    cost = models.PositiveBigIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    location = models.TextField()
    categoryid = models.UUIDField(blank=False)

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    advert_id = models.UUIDField(default=uuid.uuid4)
    image_id = models.UUIDField(default=uuid.uuid4)
    image = models.TextField()

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.UUIDField(blank=False)
    advert_id = models.UUIDField(blank=False)
    text = models.TextField()
