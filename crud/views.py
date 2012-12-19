from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
	return render_to_response("crud/index.html", context_instance=RequestContext(request))
	
def about(request):
	return render_to_response("crud/about.html", context_instance=RequestContext(request))