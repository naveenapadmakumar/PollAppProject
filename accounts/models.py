from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_staff = True  # Set the user as staff
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_staff = True  # Set the user as staff
        user.is_superuser = True  # Set the user as a superuser
        user.save(using=self._db)
        return user

class RegisterModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150,null=True,blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=60)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # User is staff by default
    is_superuser = models.BooleanField(default=False)  # User is not a superuser by default

    # Define the fields that are required when creating a user
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email



