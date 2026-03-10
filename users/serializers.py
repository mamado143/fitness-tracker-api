from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Make sure the password doesn't get returned in the API response
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        # We use our custom create_user method so the password gets properly hashed
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
