from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Interface Django with custom UserProfile."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        # Check for REQUIRED_FIELDS
        if not email:
            raise ValueError('Users must have an email address.')

        # Normalise email input
        email = self.normalize_email(email)

        # Create user object
        user = self.model(email=email, name=name)

        # Create hashed password object
        user.set_password(password)

        # Save the user object
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates a new superuser"""

        # create standard user object
        user = self.create_user(email, name, password)

        # Set extra settings for superuser
        user.is_superuser = True
        user.is_staff = True

        # Save user object
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent custom a "user profile" inside system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Set object manager
    objects = UserProfileManager()

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


class ProfileFeedItem(models.Model):
    """Represent a feed/status item."""

    # Create a foreign key to link UserProfile and ProfileFeedItem
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

    # Create a feed text field
    feed_text = models.CharField(max_length=255)

    # Create a datetime asssociated time created
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the model as a string."""
        return self.feed_text
