from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response

class ProductAPIView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.
