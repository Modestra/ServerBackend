from django.db import models
import uuid, jwt, datetime
from django.conf import settings

class AdminModel(models.Model):
    id = models.AutoField(primary_key=True)
    fio = models.TextField()

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    second_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    date = models.TextField()
    phone = models.CharField(max_length=20)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.UUIDField(default=uuid.uuid4)
    medic_id = models.UUIDField()
    date = models.TextField()
    time = models.TextField()
    sum_order = models.IntegerField()
    status = models.CharField(max_length=30)

class Medicament(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    money = models.IntegerField()
    instruction = models.TextField()

class HistoryOrder(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.UUIDField()


