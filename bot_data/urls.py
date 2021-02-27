from django.urls import path
from .laisha2 import Material
from .views import index

urlpatterns = [
    path('laisha2/material/', Material.as_view())
]
