from unittest import TestCase

from django.test import TestCase as DjangoTestCase
from django.urls import resolve, reverse
from todolist import views


class TestsTodoListUnittest(TestCase):
    def test_url_todolist(self):
        url = reverse('todolist:painel')
        self.assertEqual('/todolist/painel/', url)

    def test_painel_view_todolist(self):
        url = reverse('todolist:painel')
        response = resolve(url)
        self.assertIs(views.painel, response.func)


class TestTodoListDjango(DjangoTestCase):
    def test_painel_view_loads_template_is_correct(self):
        url = reverse('todolist:painel')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'todolist/pages/painel.html')
