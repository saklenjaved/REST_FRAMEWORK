from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.getRoutes),
    path('api/addtask/', views.addTask),
    path('api/viewtasks/', views.viewTasks),
    path('api/updatetask/<str:task_id>/', views.updateTask),
    path('api/deletetask/<str:task_id>/', views.deleteTask),
    
    path('api/viewcategories/', views.viewCategories),
]
