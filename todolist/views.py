from django.shortcuts import redirect, render

from .models import Task


def painel(request):
    completed_tasks = Task.objects.filter(
        is_completed=True).order_by('last_updated')
    uncompleted_tasks = Task.objects.filter(
        is_completed=False).order_by('id')

    return render(request, 'todolist/pages/painel.html', context={
        'completed_tasks': completed_tasks,
        'uncompleted_tasks': uncompleted_tasks,
    })


def done(request):
    id_task = request.GET.get('task_id')

    task = Task.objects.get(pk=id_task)
    task.is_completed = True
    task.save()

    return redirect('todolist:painel')


def undone(request):
    id_task = request.GET.get('task_id')

    task = Task.objects.get(pk=id_task)
    task.is_completed = False
    task.save()

    return redirect('todolist:painel')
