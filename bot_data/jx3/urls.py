from django.urls import path
from .views import RiChang

urlpatterns = [
    path('richang/', RiChang.as_view())
]
