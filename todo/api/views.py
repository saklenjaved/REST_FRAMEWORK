from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .serializers import TaskSerializer
from rest_framework.response import Response
from core.models import Tasks


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET api/',
        'POST api/addtask/',
        'GET api/viewtasks/',
        'PATCH api/updatetask/<str:task_id>/',
        'DELEtE api/deletetask/<str:task_id>/',
    ]
    return Response(routes)

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