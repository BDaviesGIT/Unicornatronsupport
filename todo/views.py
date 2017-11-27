# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from todo.serializers import TodoSerializer
from todo.models import Todo

def todo(request):
    todo = Todo.objects.all()[:10]

    context = {
        'todo':todo
    }
    return render(request, 'todo.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']

        todo = Todo(title=title, description=description)
        todo.save()

        return redirect('/todo/')
    else:
		return render(request, 'add.html')



class TodoView(APIView):

    def get(self, request, pk=None):
        if pk is None:
            todo_items = Todo.objects.all()
            # Serialize the data retrieved from the DB and serialize
            # them using the `TodoSerializer`
            serializer = TodoSerializer(todo_items, many=True)
            # Store the serialized data `serialized_data`
            serialized_data = serializer.data
            return Response(serialized_data)
        else:
            # Get the object containing the pk provided by the URL
            todo = Todo.objects.get(id=pk)
            # Serialize the `todo` item
            serializer = TodoSerializer(todo)
            # Store it in the serialized_data variable and return it
            serialized_data = serializer.data
            return Response(serialized_data)

    def post(self, request, pk):
        serializer = TodoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo, data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, pk):
        todo = Todo.objects.get(id=pk)
        todo.delete()
	return Response(status=status.HTTP_204_NO_CONTENT)