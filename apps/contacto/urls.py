from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.contacto.views',
    url(r'^$', 'index'),
	url(r'^agregar$', 'agregar'),
	url(r'^editar/(?P<id>\d+)$', 'editar'),
	url(r'^borrar/(?P<id>\d+)$', 'borrar'),
)
