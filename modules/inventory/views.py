from django.shortcuts import render, get_object_or_404
from modules.accounts.models import Customer
from modules.inventory.models import Category, Product, Rating
from rest_framework import generics, serializers, status, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from modules.accounts.permissions import IsAdministrator, IsCustomer
from modules.inventory.serializers import (
    CategorySerializer, ProductSerializer,
    RatingSerializer)
from django.db.models import Q


class ProductAPIView(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAdministrator, IsCustomer]
    http_method_names = ["get", "put", "post", "patch", "delete"]

    def get_queryset(self):
        productQs = Product.objects.all()
        return productQs

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user.role == "Administrator":
            print(serializer)
            serializer.save()
        else:
            return Response(
                {"message": "You are not authorized to perform this action."},
                status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(
            queryset, data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        print(serializer.is_valid)
        if request.user.role == "Administrator":
            productObj = Product.objects.get(pk=request.data["id"])
            print(request.data["category"])
            categoryQuery = Category.objects.get(
                id=request.data["category"])
            productObj.category = categoryQuery
            productObj.save()
            serializer.save()
        else:
            return Response(
                {"message": "You are not authorized to perform this action."},
                status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = get_object_or_404(queryset, pk=pk)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CategoryAPIView(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAdministrator, IsCustomer]
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user.role == "Administrator":
            serializer.save()
        else:
            return Response(
                {"message": "You are not authorized to perform this action."},
                status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(
            queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if request.user.role == "Administrator":
            serializer.save()
        else:
            return Response(
                {"message": "You are not authorized to perform this action."},
                status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = get_object_or_404(queryset, pk=pk)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class RatingAPIView(ModelViewSet):
    serializer_class = RatingSerializer
    permission_classes = [IsCustomer]
    http_method_names = ["get", "post", "put"]

    def get_queryset(self):
        user = self.user
        customerQuery = Customer.objects.get(user=user)
        ratingQs = Rating.objects.filter(
            Q(customer=customerQuery)
        )
        return ratingQs

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customerQs = Customer.objects.get(user=request.user)
        serializer.save(customer=customerQs)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(
            queryset, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        customerQs = Customer.objects.get(user=request.user)
        serializer.save(customer=customerQs)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = get_object_or_404(queryset, pk=pk)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
