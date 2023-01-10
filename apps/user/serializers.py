from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "pkid",
            "first_name",
            "last_name",
            "email",
            "phone",
            "country",
            "is_active",
            "is_verified",
            "account_activation_otp",
            "reset_password_otp",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            phone=validated_data["phone"],
            country=validated_data["country"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
