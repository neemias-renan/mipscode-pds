# Generated by Django 4.1.3 on 2022-12-29 19:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=150)),
                ('bio', models.TextField(default='Biografia do Usuário')),
                ('avatar', models.ImageField(upload_to='media/avatar')),
                ('user_type', models.CharField(choices=[('1', 'Admin'), ('2', 'Student'), ('3', 'Teacher')], default='2', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ide_theme', models.CharField(choices=[('1', 'Dark'), ('2', 'Light')], default='1', max_length=1)),
                ('language', models.CharField(choices=[('1', 'Português'), ('2', 'Inglês')], default='1', max_length=1)),
                ('email_notification', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mipscode.usernew')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=300)),
                ('content', models.JSONField(null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 29, 19, 22, 22, 643150, tzinfo=datetime.timezone.utc), verbose_name='Created Date')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mipscode.usernew')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('content', models.JSONField(null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 29, 19, 22, 22, 643150, tzinfo=datetime.timezone.utc), verbose_name='Created Date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mipscode.usernew')),
            ],
        ),
    ]