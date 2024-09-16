from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
import random
from django.utils import timezone
from datetime import timedelta

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('generic', 'Generic'),
        ('farmer', 'Farmer'),
        ('researcher', 'Researcher'),
        ('investor', 'Investor'),
        ('gov', 'Government Agency'),
        ('ngo', 'Non-Governmental Organization'),
        ('provider', 'Service Provider'),
    )
    username = models.CharField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='users/profile', null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='generic')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['user_type']

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.user_type})'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    

    @property
    def profile(self):
        profile = {
            'generic': self.generic_profile,
            'farmer': self.farmer_profile,
            'researcher': self.researcher_profile,
            'investor': self.investor_profile,
            'gov': self.gov_profile,
            'ngo': self.ngo_profile,
            'provider': self.provider_profile,

        }

        return profile[self.user_type]