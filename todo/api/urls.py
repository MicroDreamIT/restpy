from django.urls import path
from todo.api import views

app_name = 'todo'

urlpatterns = [
    path('', views.TodoListApiView.as_view(), name='indexTodoApi')
]