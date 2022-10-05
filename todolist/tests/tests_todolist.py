from unittest import TestCase
from urllib import response

# from django.test import TestCase as DjangoTestCase
from django.urls import resolve, reverse


class TestsTodoList(TestCase):
    def test_url_todolist(self):
        url = reverse('todolist:painel')
        self.assertEqual('/todolist/painel/', url)

    def test_home_view_todolist(self):
        url = reverse('todolist:painel')
        response = resolve(url)
        self.assertIs(views.painel, response.func)
