from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def welcomeMeasures(request):
        return HttpResponse("Measures index  page")

