from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task = models.CharField(max_length=100)
    
    def __str__(self):
        return self.task 
