from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#home_page = None
def home_page(request):
	#pass
	return HttpResponse('<html><title>To-Do lists</title><body><h1>Nama To-Do saya Khusna Nadia</h1></body></html>')
