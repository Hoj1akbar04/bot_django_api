

from django.shortcuts import render
from django.views import View
from .models import Users, Product


class UsersView(View):
    def get(self, request):
        users = Users.objects.all()
        context = {
            'users': users
        }
        return render(request, 'users.html', context)


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products.html', {'products': products})

