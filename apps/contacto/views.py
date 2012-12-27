from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

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


def detalle(request, id):
	contacto = Contacto.objects.get(pk=id)
	return render_to_response("contacto/detalle.html", { "contacto": contacto }, context_instance=RequestContext(request))


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


def pdf(request):
	response = HttpResponse(mimetype='application/pdf')
	response['Content-Disposition'] = 'filename="listado_contactos.pdf"'

	buffer = BytesIO()
	doc = SimpleDocTemplate(buffer, pagesize=letter)
	elements = []
	style = ParagraphStyle(
		name='Normal',
		fontName='Helvetica-Bold',
		fontSize=12,
		alignment=TA_CENTER
	)
	elements.append(Paragraph("LISTADO DE CONTACTOS", style))
	elements.append(Spacer(1, 1 * cm))
	
	data= [['Nombre Completo', 'F/N', 'email', 'twitter']]
	for c in Contacto.objects.all():
		data.append([
			c.nombre_completo(),
			c.fn,
			c.email,
			c.twitter
		])
		
	columnas = [240, 70, 120, 100]
	
	t=Table(data, columnas)
	t.setStyle(TableStyle([
		('ALIGN' , (0, 0), (3, 0), 'CENTER'),		
		('VALIGN', (0, 0), (3, 0), 'MIDDLE'),
		('ALIGN', (0, 1), (-1, -1), 'LEFT'),
		('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
		('BOX', (0, 0), (-1, -1), 0.25, colors.black),
		('BACKGROUND', (0, 0), (3, 0), colors.gray),
	]))
	elements.append(t)
	
	doc.build(elements)
	response.write(buffer.getvalue())
	buffer.close()
	return response
