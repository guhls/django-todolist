from django.urls import path

from . import views

app_name = 'todolist'

urlpatterns = [
    path('painel/', views.painel, name='painel')
]
