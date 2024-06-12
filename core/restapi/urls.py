from django.urls import path
from .views import ProductAPIViewSet

urlpatterns = [
    path('products', ProductAPIViewSet.as_view(), name='products'),
]