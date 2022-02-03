from django.urls import path
from accounts.views.api_views import (LoginViewSet,
                                      CustomerRegistrationViewSet,
                                      RefreshViewSet, VerifyEmail,
                                      RequestPasswordResetEmail,
                                      PasswordResetTokenCheck,
                                      SetNewPasswordAPIView
                                      )
from django.views.generic import TemplateView
from rest_framework.routers import SimpleRouter
app_name = "api"
routes = SimpleRouter()
routes.register("login",
                LoginViewSet,
                basename="login")
routes.register("customer/signup",
                CustomerRegistrationViewSet,
                basename="customerSignup")
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')
routes.register('password-reset', RequestPasswordResetEmail,
                basename="requestPasswordReset")
routes.register('password-reset-complete',  SetNewPasswordAPIView,
                basename="password-reset-complete")

urlpatterns = [
    *routes.urls,
    path('activate/', VerifyEmail,
         name="email-verify"),
    path("password-reset/<uidb64>/<token>/",
         PasswordResetTokenCheck,
         name="password-token-check"),
    path('password-reset-successful/',
         TemplateView.as_view(
             template_name="accounts/password_reset_success.html"),
         name="passwordResetSuccess"
         )

]
