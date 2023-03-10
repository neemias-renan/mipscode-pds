# Generated by Django 4.1.3 on 2023-01-25 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipscode', '0010_alter_repositorio_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositorio',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 25, 17, 42, 26, 662417, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='repositorio',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 25, 17, 42, 26, 662417, tzinfo=datetime.timezone.utc), verbose_name='Edited Date'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='content',
            field=models.JSONField(default=''),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 25, 17, 42, 26, 661418, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
    ]
