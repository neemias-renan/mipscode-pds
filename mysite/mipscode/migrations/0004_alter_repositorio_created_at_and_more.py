# Generated by Django 4.1.3 on 2023-01-05 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipscode', '0003_repositorio_alter_tutorial_created_at_delete_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositorio',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 5, 12, 7, 42, 607117, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 5, 12, 7, 42, 606118, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
    ]
