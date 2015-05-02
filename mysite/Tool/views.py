from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Template, Context, RequestContext
# Create your views here.

def welcomeTool(request):
        return render_to_response('dummyTool.html', context_instance=RequestContext(request))
def resultPage(request):
        input = request.POST['Pollutant']
        return render_to_response('AQIResult.html', {'Pollutant': input}, context_instance=RequestContext(request))
