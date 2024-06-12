from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


from restapi.serializers import ProductSerializer
from products.models import Product


class ProductAPIViewSet(APIView):
    def get_queryset(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


