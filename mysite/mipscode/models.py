import datetime
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from PIL import Image


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, name, email, password, bio, avatar, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True. ')

        return self.create_user(name, email, password, bio, avatar, **other_fields)

    def create_user(self, name, email, password, bio, avatar, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email addres'))

        email = self.normalize_email(email)
        user = self.model( name=name,email=email, password=password,
                          bio=bio, avatar=avatar, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=150)
    bio = models.TextField(default='Biografia do Usuário')
    avatar = models.ImageField(
        upload_to='media/avatar', default='media/avatar/default.jpg')
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    types_users = [
        ('1', 'Admin'),
        ('2', 'Student'),
        ('3', 'Teacher'),
    ]

    user_type = models.CharField(
        max_length=1, choices=types_users, default='2')


    object = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','bio','avatar']


class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    types_themes = [
        ('1', 'Dark'),
        ('2', 'Light'),
    ]

    languages = [
        ('1', 'Português'),
        ('2', 'Inglês'),
    ]

    ide_theme = models.CharField(
        max_length=1, choices=types_themes, default='1')
    language = models.CharField(max_length=1, choices=languages, default='1')
    email_notification = models.BooleanField(default=True)


class Tutorial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    content = models.JSONField(null=True)

    created_at = models.DateTimeField('Created Date', default=timezone.now())

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data <= now

    def __str__(self):
        return self.title


class Project(models.Model):

    def content_default():
        return {"code": ""}


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    # alterar para JSONField() e salvar o objeto 'sys' daquele projeto como json
    content = models.JSONField(null=True, default=content_default)
    created_at = models.DateTimeField('Created Date', default=timezone.now())

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data <= now

    def __str__(self):
        return self.title


class Documentation(models.Model):
    title = models.CharField(max_length=50)
    content = models.JSONField(null=True)

    def __str__(self):
        return self.title
