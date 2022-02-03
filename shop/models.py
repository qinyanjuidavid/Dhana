from django.db import models
from accounts.models import User, Administrator, Customer, TrackingModel
from django.utils.translation import gettext as _
from django.utils import timezone
from django.core.validators import (
    MaxLengthValidator,
    MaxValueValidator,
    MinLengthValidator)


class Category(TrackingModel):
    category = models.CharField(_("category"),
                                max_length=67,
                                unique=True)
    added_by = models.ForeignKey(Administrator,
                                 on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"


class Brand(TrackingModel):
    brand = models.CharField(_("brand"),
                             max_length=89, unique=True
                             )
    added_by = models.ForeignKey(Administrator,
                                 on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.brand


class Product(TrackingModel):
    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Bisexual", "Bisexual")
    )
    product = models.CharField(_("product name"),
                               max_length=156)
    gender = models.CharField(_("gender"),
                              max_length=15, choices=gender_choices)
    image = models.ImageField(_("image"),
                              upload_to="products/")
    price = models.FloatField(_("price"))
    discount_price = models.FloatField(_("discount price"), default=0.00)
    description = models.TextField(_("description"),
                                   blank=True, null=True)
    size = models.FloatField(_("shoe size"))
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand,
                              on_delete=models.DO_NOTHING,
                              blank=True, null=True)
    color = models.CharField(_("shoe color"),
                             max_length=20,)
    number_of_pairs = models.PositiveIntegerField(_("number of pairs"),
                                                  default=0)
    available = models.BooleanField(_("available"), default=True)
    added_by = models.ForeignKey(Administrator,
                                 on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product


class Rating(TrackingModel):
    product = models.ForeignKey(Product, related_name="products",
                                on_delete=models.CASCADE)
    rating = models.IntegerField(_("rating"),
                                 default=0, validators=[
        MaxValueValidator(5),
        MinLengthValidator(0)])
    review = models.TextField(blank=True, null=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.user.username}-{self.product.product}"


class OrderItem(TrackingModel):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(_("quantity"), default=1)
    ordered = models.BooleanField(_("quantity"), default=False)
    paid = models.BooleanField(_("paid"), default=False)
    total_price = models.FloatField(_("total price"), default=0.00)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.product


class Order(TrackingModel):
    product = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(_("ordered"), default=False)
    paid = models.BooleanField(_("paid"), default=False)
    total_price = models.FloatField(_("total price"), default=0.00)
    date_ordered = models.DateTimeField(_("date ordered"))
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.customer
