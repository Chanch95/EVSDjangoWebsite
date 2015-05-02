from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def welcomeTeam(request):
        return HttpResponse("Team index  page")

