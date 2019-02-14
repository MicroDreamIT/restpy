from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoListApiView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


def index(request):
    return render(request, 'index.html')
