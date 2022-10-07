from django.shortcuts import redirect, render

from .models import Task, User


def painel(request):
    completed_tasks = Task.objects.filter(
        is_completed=True).order_by('last_updated')
    uncompleted_tasks = Task.objects.filter(
        is_completed=False).order_by('id')

    return render(request, 'todolist/pages/painel.html', context={
        'completed_tasks': completed_tasks,
        'uncompleted_tasks': uncompleted_tasks,
    })


def task_view(request, id):
    task = Task.objects.get(pk=id)

    return render(request, 'todolist/pages/task-view.html', context={
        'task': task,
    })


def edit(request):
    task_id = request.GET.get('task-id')
    task_title = request.GET.get('task-title')

    task = Task.objects.get(pk=task_id)
    task.title = task_title
    task.save()

    return redirect('todolist:painel')


def create_view(request):
    title = request.GET.get('new-card-title')
    user = User.objects.get(pk=request.user.pk)

    Task.objects.create(title=title, author=user)

    return redirect('todolist:painel')


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


def delete(request):
    id_task = request.GET.get('task_id')

    task = Task.objects.get(pk=id_task)
    task.delete()

    return redirect('todolist:painel')
