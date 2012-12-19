from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from contacto.models import Contacto
from contacto.forms import ContactoForm


def index(request):
	contactos = Contacto.objects.all()
	return render_to_response("contacto/index.html", { "contactos": contactos }, context_instance=RequestContext(request))

def agregar(request):
	if request.method == 'POST':
		frm = ContactoForm(request.POST)
		if frm.is_valid():
			frm.save()
			return HttpResponseRedirect("/")
	else:
		frm = ContactoForm()
	return render_to_response("contacto/agregar.html", { "frm": frm }, context_instance=RequestContext(request))

#def editar(request):


#def borrar(request):