from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.contacto.models import Contacto
from apps.contacto.forms import ContactoForm


def index(request):
	contactos = Contacto.objects.all()
	return render_to_response("contacto/index.html", { "contactos": contactos }, context_instance=RequestContext(request))

def agregar(request):
	if request.method == 'POST':
		frm = ContactoForm(request.POST)
		if frm.is_valid():
			frm.save()
			return HttpResponseRedirect("/contacto")
	else:
		frm = ContactoForm()
	return render_to_response("contacto/agregar.html", { "frm": frm }, context_instance=RequestContext(request))

def editar(request, id):
	contacto = Contacto.objects.get(pk=id)
	if request.method == 'POST':
		frm = ContactoForm(request.POST, instance=contacto)
		if frm.is_valid():
			frm.save()
			return HttpResponseRedirect("/contacto")
	else:
		frm = ContactoForm(instance=contacto)
	return render_to_response("contacto/editar.html", { "frm": frm }, context_instance=RequestContext(request))


def borrar(request, id):
	contacto = Contacto.objects.get(pk=id)
	contacto.delete()
	return HttpResponseRedirect("/contacto")