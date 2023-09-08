from rest_framework import serializers
from .models import Todo_Model

class Todo_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Todo_Model
        fields = ("task_name","createdat","updatedat","status","description")
    