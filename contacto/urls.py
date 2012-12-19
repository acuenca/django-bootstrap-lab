from django.conf.urls import patterns, include, url


urlpatterns = patterns('contacto.views',
    url(r'^index$', 'index'),
	url(r'^agregar$', 'agregar'),
)
