from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def welcomeGetUpdates(request):
        return HttpResponse("GetUpdates index page")

