from django.urls import path, include
from .laisha2 import urls as laisha2_url
from .jx3 import urls as jx3_url
from .views import index

urlpatterns = [
    path('', index),
    path('laisha2/', include(laisha2_url)),
    path('jx3/', include(jx3_url))
]
