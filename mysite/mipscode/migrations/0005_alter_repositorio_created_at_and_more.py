# Generated by Django 4.1.2 on 2023-01-17 20:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipscode', '0004_profile_name_alter_repositorio_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositorio',
            name='created_at',
            field=models.DateTimeField(default='2023-01-17 20:28:19', verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 17, 20, 28, 19, 565399, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
    ]
