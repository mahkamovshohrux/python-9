from django.shortcuts import render, get_object_or_404
from .models import Todo_Model
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Todo_Serializers


# Create your views here.

class TodoList(APIView):
    def get(self,request):
        to_deta = Todo_Model.objects.all()
        todo1 = Todo_Serializers(to_deta,many=True)
       
        return Response(todo1.data)


class CreatTodo(APIView):
    def post(self,request):
        creattodo = Todo_Serializers(data=request.data)
        if creattodo.is_valid:
            creattodo.save()
            return Response(creattodo.data)
        return Response({creattodo.errors})
    
class TodoUpdate(APIView):
    def patch(self, request, *args, **kwargs):
        up = get_object_or_404(Todo_Model, id=kwargs['todo_id'])
        updatetodo = Todo_Serializers(up, data=request.data,partial=True)
        if updatetodo.is_valid:
            updatetodo.save()
            return Response(updatetodo.data)
        return Response({updatetodo.errors})

class DeletTodo(APIView):
    def delete(self, request, *args, **kwargs):
        deletetudo = get_object_or_404(Todo_Model,id=kwargs['todo_id'])
        deletetudo.delete()
        return Response({"msg":"successfully delete"})