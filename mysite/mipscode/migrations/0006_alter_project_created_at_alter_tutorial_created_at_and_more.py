# Generated by Django 4.1.3 on 2022-12-27 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipscode', '0005_alter_project_created_at_alter_tutorial_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 27, 18, 52, 10, 494113, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 27, 18, 52, 10, 493114, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
    ]
