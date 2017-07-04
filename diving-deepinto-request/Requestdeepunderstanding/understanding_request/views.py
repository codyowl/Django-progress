from django.shortcuts import render, render_to_response
from django.http import HttpResponse


# Create your views here.
def request_dot_GET(request, template='request_dot_GET.html'):
	q_value = request.GET
	print q_value
	return render_to_response(template)