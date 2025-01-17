from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from .models import Status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,filters
from .serializer import statusSerializer
# Create your views here.
@api_view(['GET','POST'])
def myfun(request):
    if request.method == 'GET':
        data = Status.objectsdjsd.all()
        serializer = statusSerializer(data,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = statusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def myfun1(request,pk):
    try:
        data = Status.objects.get(pk=pk)
    except status.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = statusSerializer(data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = statusSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)