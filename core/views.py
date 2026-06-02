from django.shortcuts import render, redirect
from .models import Tasks, Category
from .forms import TaskForm, CategoryForm
from django.db.models import Q

# Create your views here.

def addCategory(request):
    if request.method == 'GET':
        categoryform = CategoryForm()
        return render(request, 'addcategory.html', {'categoryform': categoryform})
    elif request.method == 'POST':
        categoryform = CategoryForm(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('/')
        return render(request, 'addcategory.html', {'categoryform': categoryform})

def editCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'GET':
        editcategory = CategoryForm(instance=category)
        return render(request, 'edit_category.html', {'editcategory': editcategory})
    elif request.method == 'POST':
        editcategory = CategoryForm(request.POST, instance=category)
        if editcategory.is_valid():
            editcategory.save()
            return redirect('/')
        return render(request, 'edit_category.html', {'editcategory': editcategory})
    
def deleteCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('/')
    
def addTask(request):
    if request.method == 'GET':
        taskform = TaskForm()
        categoryform = CategoryForm
        tasks = Tasks.objects.all()    
        categories = Category.objects.all()
        search = request.GET.get('search', '').strip()
        if search:
            tasks = Tasks.objects.filter(
            Q(title__icontains=search) | 
            Q(category__name__icontains=search)
            )
        else:
            tasks = Tasks.objects.all()
            
        return render(request, 'addtask.html', {'taskform': taskform, 'tasks': tasks, 'categoryform': categoryform, 'categories': categories})
    
    elif request.method == 'POST':
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            taskform.save()
            return redirect('/')
        
        return render(request, 'addtask.html', {'taskform': taskform, 'tasks': tasks, 'categoryform': categoryform, 'categories': categories})

def viewTasks(request):
    tasks = Tasks.objects.all()
    return render(request, 'viewtasks.html', {'tasks': tasks})

def editTask(request, task_id):
    task = Tasks.objects.get(id=task_id)
    if request.method == 'GET':
        edit_taskform = TaskForm(instance=task)
        return render(request, 'edit_task.html', {'edit_taskform':edit_taskform})
    
    elif request.method == 'POST':
        edit_taskform = TaskForm(request.POST, instance=task)
        if edit_taskform.is_valid():
            edit_taskform.save()
            return redirect('/')
        return render(request, 'edit_task.html', {'edit_taskform': edit_taskform})
    
def deleteTask(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('/')