from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext


# Create your views here.
#request.GET
def request_dot_GET(request, template='request_dot_GET.html'):
	g_value = request.GET
	print g_value
	return render_to_response(template)

def request_dot_GET_dot_get(request, template='request_dot_GET.html'):
	g_value = request.GET.get('g')
	print g_value
	return render_to_response(template) 	

def request_dot_GET_parameter(request, template='request_dot_GET.html'):
	if 'g' in request.GET:
		g_value = request.GET['g']
	else:
		g_value = False
	print g_value
	return render_to_response(template)

#request.POSt
def request_dot_POST(request, template='request_dot_POST.html'):
	p_value = request.POST	
	print p_value
	return render_to_response(template, context_instance=RequestContext(request))	

def request_dot_POST_dot_get(request, template='request_dot_POST.html'):
	p_value = request.POST.get('p') #since p is the name of text box 	
	print p_value
	return render_to_response(template, context_instance=RequestContext(request))		

def request_dot_POST_parameter(request, template='request_dot_POST.html'):
	p_value = request.POST['p']#since p is the name of text box 	
	print p_value
	return render_to_response(template, context_instance=RequestContext(request))			