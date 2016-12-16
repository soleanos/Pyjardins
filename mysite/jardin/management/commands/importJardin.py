from django.core.management.base import BaseCommand, CommandError
from jardin.models import Parc
import json
class Command(BaseCommand):
	help = 'json jardin'

	def handle(self, *args, **kwargs):
		with open("D:/Users/aarchamb/Desktop/python/parc.json", "r", encoding="utf-8") as f:
			j = json.loads(f.read())
			for jardin in j['data']:
				parcObject = Parc(code=jardin['Code'], commentaire=jardin['Commentaire'],adresse=jardin['adresse_postale'] )
				#~ print(parcObject.commentaire)
				parcObject.save()

