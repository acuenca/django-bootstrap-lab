from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^$', 'crud.views.index'),
	url(r'^about$', 'crud.views.about'),
	url(r'^contacto/', include('apps.contacto.urls')),
)
