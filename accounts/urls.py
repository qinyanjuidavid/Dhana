from django.urls import path
from accounts.views.templating_views import (
    AdministratorSignupView, CustomerSignupView,
    RequestPasswordReset)
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("administrator/signup/", AdministratorSignupView.as_view(),
         name="adminSignup"),
    path("customer/signup/", CustomerSignupView.as_view(),
         name="customerSignup"),

    # Login and Logout paths
    path('login/', auth_views.LoginView.as_view(
        template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name="accounts/logout.html"), name="logout"),
    path("request-password-reset/", RequestPasswordReset,
         name="RequestPasswordReset"
         )
]
