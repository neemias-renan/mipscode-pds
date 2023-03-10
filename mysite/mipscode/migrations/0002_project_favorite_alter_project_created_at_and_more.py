# Generated by Django 4.1.3 on 2022-12-29 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipscode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 29, 22, 12, 19, 284971, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 29, 22, 12, 19, 284971, tzinfo=datetime.timezone.utc), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='usernew',
            name='avatar',
            field=models.ImageField(default='avatar/default.jpg', upload_to='avatar'),
        ),
    ]
