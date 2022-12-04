from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    pass


class Organization(models.Model):
    name = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    users = models.ManyToManyField(User, related_name="organizations")
    personal = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


class Application(models.Model):
    organization = models.ForeignKey(
        Organization, related_name="applications", on_delete=models.RESTRICT
    )
    name = models.TextField()
    slug = models.SlugField(max_length=100)
    active = models.BooleanField(default=True)


class ApiKey(models.Model):
    application = models.ForeignKey(
        Application, related_name="api_keys", on_delete=models.CASCADE
    )
    version = models.TextField()
    api_key = models.TextField()
    active = models.BooleanField(default=True)
