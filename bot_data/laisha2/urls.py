from django.urls import path
from . import Material

urlpatterns = [
    path('material/', Material.as_view())
]
