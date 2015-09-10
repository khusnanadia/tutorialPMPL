from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.

#class SmokeTest(TestCase):
#	def test_bad_maths(self):
#		self.assertEqual(1+1,3)

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>To-Do lists</title><body><h1>Nama To-Do saya Khusna Nadia</h1></body>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
