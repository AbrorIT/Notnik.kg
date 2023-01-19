from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from threading import Thread
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    profele_image = models.ImageField(upload_to= "profile_image/", null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользлватели"


