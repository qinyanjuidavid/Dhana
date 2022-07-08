from rest_framework.routers import SimpleRouter
from django.urls import path


app_name = "api"
routes = SimpleRouter()


urlpatterns = [
    *routes.urls,
]
