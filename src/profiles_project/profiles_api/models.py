from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from djange.contrib.auth.models import PermissionsMixin


# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent custom a "user profile" inside system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Set object manager
    object = UserProfileManager()

    # Overwrite the username field from name to email (required by default)
    USERNAME_FIELD = 'email'

    # Define required fields
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Get the user's full name."""
        return self.name

    def get_short_name(self):
        """Get the user's short name."""
        return self.name

    def __str__(self):
        """For Django to convert object to a string."""
        return self.email
