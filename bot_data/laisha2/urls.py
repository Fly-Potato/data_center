from django.urls import path
from .views import Material

urlpatterns = [
    path('material/', Material.as_view())
]
