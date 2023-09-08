from django.db import models

# Create your models here.
class Todo_Model(models.Model):
    task_name = models.CharField(max_length=125)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=False)
    description = models.CharField(max_length=100)