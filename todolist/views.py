from django.shortcuts import render

from .models import Task


def painel(request):
    completed_tasks = Task.objects.filter(
        author__username=request.user.username, is_completed=True)
    uncompleted_tasks = Task.objects.filter(
        author__username=request.user.username, is_completed=False)

    return render(request, 'todolist/pages/painel.html', context={
        'completed_tasks': completed_tasks,
        'uncompleted_tasks': uncompleted_tasks,
    })
