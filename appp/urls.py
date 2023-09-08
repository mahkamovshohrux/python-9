from django.urls import path
from .views import TodoList, TodoDetail,CreatTodo,TodoUpdate,DeletTodo


urlpatterns = [
    path("listtodo/",TodoList.as_view()),
    path("detail/<int:todo_id>",TodoDetail.as_view()),
    path("creat/", CreatTodo.as_view()),
    path("updata/<int:todo_id>",TodoUpdate.as_view()),
    path("delete/<int:todo_id>",DeletTodo.as_view()),

]