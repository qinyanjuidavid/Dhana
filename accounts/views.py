from django.shortcuts import render
from accounts.models import (User, Administrator, Customer)
from accounts.serializers import (
    UserSerializer, CustomerRegistrationSerializer)
