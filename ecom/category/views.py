from django.shortcuts import render
from category.models import Category
from rest_framework.views import APIView
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import permissions
# Create your views here.
class CategoryAPIView(APIView):
    # permission_classes = [permissions.AllowAny, ]
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Todo with given todo data
    #     '''
    #     data = {
    #         'task': request.data.get('task'), 
    #         'completed': request.data.get('completed'), 
    #         'user': request.user.id
    #     }
    #     serializer = CategorySerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)