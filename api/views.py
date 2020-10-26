from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def cook_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        cooks = Cook.objects.all()
        serializer = CookSerializer(cooks, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = CookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getCook(request, pk):
    """
    Retrieve, update or delete a cook instance.
    """
    try:
        cook = Cook.objects.get(pk=pk)
    except Cook.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CookSerializer(cook, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CookSerializer(cook, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
