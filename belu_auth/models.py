from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class BeluUser(AbstractUser):
    username = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class BeluUserProfile(models.Model):
    user = models.OneToOneField(BeluUser, on_delete=models.CASCADE, related_name='belu_user_profile')
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    document = models.CharField(max_length=20)
    birth_date = models.DateField()
    phone = models.CharField(max_length=255)
