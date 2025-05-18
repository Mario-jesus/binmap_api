# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username", "password", "first_name", "last_name"]
