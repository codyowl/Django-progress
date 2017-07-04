from django.shortcuts import render, render_to_response
from django.http import HttpResponse


# Create your views here.
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