from django.urls import path
from .views import UsersView, ProductsView

urlpatterns = [
    path('users', UsersView.as_view(), name='users'),
    path('product', ProductsView.as_view(), name='product'),
]