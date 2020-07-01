from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name filed for testing APIViews."""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for the UserProfile objects."""

    class Meta:
        # Tell Django RF that this model serializer is going
        # to be used as the model
        model = models.UserProfile
        fields = (
            'id',
            'email',
            'name',
            'password'
        )
        # Make sure the passwards are never read
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(email=validated_data['email'], name=validated_data['name'])

        # Create and assign the hashed password
        user.set_password(validated_data['password'])

        # Save to DB
        user.save()

        return user
