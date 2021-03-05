from django.urls import path
from .views import API

urlpatterns = [
    path('<module>/', API.as_view())
]
