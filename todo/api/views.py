from rest_framework.generics import ListAPIView
from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoListApiView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
