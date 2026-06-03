from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .serializers import TaskSerializer, CategorySerializer
from rest_framework.response import Response
from core.models import Tasks, Category


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET api/',
        'POST api/addtask/',
        'GET api/viewtasks/',
        'PATCH api/updatetask/<str:task_id>/',
        'DELETE api/deletetask/<str:task_id>/',
        
        'GET api/viewcategories/',
        'POST api/addcategory/',
        'PATCH api/editcategory/<str:category_id>/',
        'DELETE api/deletecategory/<str:category_id>/',
    ]
    return Response(routes)


@api_view(['POST'])
def addCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PATCH'])
def editCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    serializer = CategorySerializer(category, request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def deleteCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return Response("Category Deleted")

@api_view(['GET'])
def viewCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def viewTasks(request):
    tasks = Tasks.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def updateTask(request, task_id):
    tasks = Tasks.objects.get(id=task_id)
    serializer = TaskSerializer(tasks, request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def deleteTask(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return Response("Task Deleted.")