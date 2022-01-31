from django.urls import path
from accounts.views import (LoginViewSet,
                            CustomerRegistrationViewSet)

from rest_framework.routers import SimpleRouter
app_name = "api"
routes = SimpleRouter()
routes.register("login",
                LoginViewSet,
                basename="login")
routes.register("customer/signup",
                CustomerRegistrationViewSet,
                basename="customerSignup")

urlpatterns = [
    *routes.urls,

]
