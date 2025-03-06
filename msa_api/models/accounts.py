from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now
import uuid

class CustomUserManager(BaseUserManager):
    """Custom manager for CustomUser."""

    def create_user(self, email, name, password=None, **extra_fields):
        """Create and return a normal user."""
        if not email:
            raise ValueError("The Email field must be set")
        if not name:
            raise ValueError("The Name field must be set")
        if not password:
            raise ValueError("A password must be set")

        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        user = self.model(email=email, name=name, date_time_of_creation=now(), **extra_fields)
        user.set_password(password)  # Hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model."""

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_time_of_creation = models.DateTimeField(default=now, editable=False)
    is_active = models.BooleanField(default=True)  # Determines if the account is active
    is_staff = models.BooleanField(default=False)  # Determines if the user is staff
    is_superuser = models.BooleanField(default=False)  # Determines if the user is a superuser
    is_verified = models.BooleanField(default=False)  # Determines if the user has verified their email
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)  # Stores the verification token

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  

    def __str__(self):
        return self.email
