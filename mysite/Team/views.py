from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import Template, Context
# Create your views here.

def welcomeTeam(request):
        fp = open('/home/chanchal/Desktop/EVS/team.html')
        t = Template(fp.read())
        fp.close()
        html = t.render(Context({'hey'}))
        return HttpResponse(html)

