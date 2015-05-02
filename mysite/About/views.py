from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def welcomeAbout(request):
	return HttpResponse("About index page")
