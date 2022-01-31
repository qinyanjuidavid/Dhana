from wsgiref import validate
from rest_framework import serializers
from accounts.models import (User,
                             Administrator, Customer)
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login

from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.utils.encoding import (DjangoUnicodeDecodeError, force_str,
                                   smart_bytes, smart_str)
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.exceptions import AuthenticationFailed


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username",
                  "email", "full_name",
                  "phone", "timestamp")
        read_only_fields = ("id", "timestamp")


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validated[attrs]
        refresh = self.get_token(self.user)
        data["user"] = UserSerializer(self.user).data
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=28, min_length=4,
        write_only=True, required=True
    )
    password_confirmation = serializers.CharField(
        max_length=28, min_length=4,
        write_only=True, required=True
    )
    email = serializers.EmailField(
        max_length=128, required=True
    )

    class Meta:
        model = User
        fields = ("username",
                  "email", "phone", "password", "password_confirmation")

    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data["email"])
            raise serializers.ValidationError(
                "User with this email already exists!")
        except ObjectDoesNotExist:
            if (validated_data["password"] and
                validated_data["password_confirmation"] and
                    validated_data["password"] !=
                    validated_data["password_confirmation"]):
                raise serializers.ValidationError("Passwords do not match!")
            else:
                user = User.objects.create(
                    username=validated_data["username"],
                    email=validated_data["email"],
                    phone=validated_data["phone"],
                    is_active=False,
                    role="Customer"
                )
                user.set_password(validated_data["password"])
                user.save()
        return user
