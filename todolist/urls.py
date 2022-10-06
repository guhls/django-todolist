from django.urls import path

from . import views

app_name = 'todolist'

urlpatterns = [
    path('painel/', views.painel, name='painel'),
    path('create/', views.create_view, name='create'),
    path('done/', views.done, name='done'),
    path('undone/', views.undone, name='undone'),
    path('delete/', views.delete, name='delete'),
]
