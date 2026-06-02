from django.contrib import admin
from .models import Tasks, Category

# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    search_fields = ('id',)
    list_filter = ('completed',)
    
admin.site.register(Tasks, TasksAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Category, CategoryAdmin)