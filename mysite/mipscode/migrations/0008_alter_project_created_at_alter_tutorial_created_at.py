# Generated by Django 4.1.3 on 2022-12-27 21:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipscode', '0007_alter_project_created_at_alter_tutorial_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 27, 21, 5, 14, 106175, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 27, 21, 5, 14, 106175, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
    ]
