# Generated by Django 4.2.7 on 2024-10-10 06:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('second_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('date', models.TextField()),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HistoryOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.UUIDField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('money', models.IntegerField()),
                ('instruction', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.UUIDField(default=uuid.uuid4)),
                ('medic_id', models.UUIDField()),
                ('date', models.TextField()),
                ('time', models.TextField()),
                ('sum_order', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
            ],
        ),
    ]
