from django.shortcuts import render, redirect
from .models import todo
from .forms import createTodo


def home(request):
    todos = todo.objects.all()
    count = todos.count()
    todoList = []

    context = {'todos': todos,
               'count': count,
               'todoList': todoList}
    return render(request, 'home.html', context)


def addTodo(request):
    form = createTodo()
    if request.method == 'POST':
        form = createTodo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'addTodo.html', context)


def removeTodo(request, todo_id):
    finishedtodo = todo.objects.get(id=todo_id)
    finishedtodo.delete()
    return redirect('/')
