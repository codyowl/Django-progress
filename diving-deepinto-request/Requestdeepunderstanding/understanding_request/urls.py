from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = patterns('understanding_request.views',
	url(r'^request-dot-GET/$','request_dot_GET', name='request_dot_GET'),
	)