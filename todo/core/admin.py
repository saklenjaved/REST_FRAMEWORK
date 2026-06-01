from django.contrib import admin
from .models import Tasks

# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id',)
    list_filter = ('completed',)
    
admin.site.register(Tasks, TasksAdmin)