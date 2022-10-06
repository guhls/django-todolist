from unittest import TestCase

from django.test import TestCase as DjangoTestCase
from django.urls import resolve, reverse
from todolist import views
from todolist.models import Task, User


class TestsTodoListUnittest(TestCase):
    def test_url_todolist(self):
        url = reverse('todolist:painel')
        self.assertEqual('/todolist/painel/', url)

    def test_painel_view_todolist(self):
        url = reverse('todolist:painel')
        response = resolve(url)
        self.assertIs(views.painel, response.func)


class TestTodoListDjango(DjangoTestCase):
    def make_user(self, author):
        user = User.objects.create(username=author, password='pass')
        return user

    def make_task(
        self,
        title='Title task',
        author='user'
    ):
        task = Task.objects.create(
            title=title,
            author=self.make_user(author),
        )
        return task

    def test_painel_view_loads_template_is_correct(self):
        url = reverse('todolist:painel')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'todolist/pages/painel.html')

    def test_task_fild_is_completed_is_false_by_default(self):
        task = self.make_task(title='Title task', author='user')
        self.assertFalse(task.is_completed)

    def test_show_tasks_in_painel(self):
        task = self.make_task()
        url = reverse('todolist:painel')

        response = self.client.get(url)
        self.assertIn(task, response.context['uncompleted_tasks'])
