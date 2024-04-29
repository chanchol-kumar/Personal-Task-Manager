from django.contrib import admin
from Task.models import TaskModel
# Register your models here.

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ["task"]
    
admin.site.register(TaskModel,TaskModelAdmin)
