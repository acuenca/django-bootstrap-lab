from django.conf.urls import patterns, include, url


urlpatterns = patterns('contacto.views',
    url(r'^$', 'index'),
	url(r'^agregar$', 'agregar'),
)
