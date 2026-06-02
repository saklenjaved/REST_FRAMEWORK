from django.urls import path
from . import views

urlpatterns = [
    path('', views.addTask, name="addtask"),
    path('viewtasks/', views.viewTasks, name="viewtasks"),
    path('edittask/<int:task_id>/', views.editTask, name="edittask"),
    path('deletetask/<int:task_id>/', views.deleteTask, name="deletetask"),

    path('addcategory/', views.addCategory, name="addcategory"),
    path('editcategory/<int:category_id>/', views.editCategory, name="editcategory"),
    path('deletecategory/<int:category_id>/', views.deleteCategory, name="deletecategory"),
]
