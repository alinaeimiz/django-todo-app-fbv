from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'task', 'completed', 'created_date', 'updated_date']
    fields = ['user', 'task', 'completed'] 
    list_filter = ('updated_date', 'created_date','user')


admin.site.register(Task, TaskAdmin)