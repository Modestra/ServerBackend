# Generated by Django 4.2.7 on 2024-09-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarlabshop', '0002_advert_advert_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
