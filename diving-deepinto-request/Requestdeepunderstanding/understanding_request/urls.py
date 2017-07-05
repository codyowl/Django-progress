from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = patterns('understanding_request.views',
	#request.GET
	url(r'^request-dot-GET/$','request_dot_GET', name='request_dot_GET'),
	url(r'^request-dot-GET-get/$','request_dot_GET_dot_get', name='request_dot_GET_dot_get'),
	url(r'^request-dot-GET-parameter/$','request_dot_GET_parameter', name='request_dot_GET_parameter'),

	#request.POST
	url(r'^request-dot-POST/$','request_dot_POST', name='request_dot_POST'),
	url(r'^request-dot-POST-get/$','request_dot_POST_dot_get', name='request_dot_POST_dot_get'),
	url(r'^request-dot-POST-parameter/$','request_dot_POST_parameter', name='request_dot_POST_parameter'),
	)