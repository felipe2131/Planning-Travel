# Generated by Django 5.0b1 on 2024-05-15 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning_travel', '0004_hotel_token_recuperar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='token_recuperar',
            field=models.IntegerField(default=1, max_length=254),
        ),
    ]
