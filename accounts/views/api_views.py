from django.shortcuts import render
from accounts.models import (User, Administrator, Customer)
from accounts.serializers import (
    UserSerializer, CustomerRegistrationSerializer, LoginSerializer)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import (AllowAny,)
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from rest_framework_simplejwt.tokens import RefreshToken
from accounts.sendMails import (
    send_activation_mail, send_password_reset_email)
from accounts.permissions import (IsAdministrator,
                                  IsCustomer)


class LoginViewSet(ModelViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post", ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)

        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data,
                        status=status.HTTP_200_OK)


class CustomerRegistrationViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = CustomerRegistrationSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post", ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(is_active=False,
                               role="customer")
        user_data = serializer.data
        send_activation_mail(user_data, request)

        refresh = RefreshToken.for_user(user)
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return Response({
            "user": serializer.data,
            'refresh': res['refresh'],
            "token": res["access"]
        },
            status=status.HTTP_201_CREATED
        )