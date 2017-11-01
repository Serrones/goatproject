from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import *
from django.http import HttpRequest
from django.shortcuts import render




class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')

        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        #request = HttpRequest()
        #response = home_page(request)
        #expected_html = render_to_string('home.html')
        #self.assertEqual(response.content.decode(), expected_html)
        #-- This is how the book describes, but works only in Django 1.8
        
        # Bellow is for Django 1.9 or >
        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertIn('A new list item', response.content.decode())
