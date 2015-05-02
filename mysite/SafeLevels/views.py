from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def welcomeSafeLevels(request):
        return HttpResponse("SaeLevels index page")

