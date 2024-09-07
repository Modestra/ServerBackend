from django.db import models
from datetime import datetime

class Card(models.Model):
    """Карточка товара для магазина"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sell = models.DecimalField(max_digits=7, decimal_places=2)
    address = models.TextField()
    time = models.DateTimeField(default=datetime.now)
