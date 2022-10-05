from django.shortcuts import render


def painel(request):
    return render(request, 'todolist/pages/painel.html')
