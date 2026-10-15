from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass  # Priyanka replaces this (email login, UUID PK) before the first migration