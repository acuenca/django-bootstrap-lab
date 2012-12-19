from django import forms

from apps.contacto.models import Contacto


class ContactoForm(forms.ModelForm):
	class Meta:
		model = Contacto