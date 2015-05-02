
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.

def home(request):
	fp = open('/home/chanchal/Desktop/EVS/Accio.html')
        t = Template(fp.read())
        fp.close()
        html = t.render(Context({'hey'}))
        return HttpResponse(html)
