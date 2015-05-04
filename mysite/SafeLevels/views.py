from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import Template, Context

# Create your views here.

def welcomeSafeLevels(request):
         fp = open('/home/chanchal/Desktop/EVS/safe.html')
         t = Template(fp.read())
         fp.close()
         html = t.render(Context({'hey'}))
         return HttpResponse(html)

