# Generated by Django 4.2.7 on 2024-09-30 08:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('solarlabshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='advert_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
