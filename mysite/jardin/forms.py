from django.forms import ModelForm
from jardin.models import Parc

class jardinForm(ModelForm):
	class Meta:
		model = Parc
		fields = ['code', 'adresse', 'commentaire']
		
