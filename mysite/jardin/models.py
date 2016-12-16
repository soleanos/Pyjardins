from django.db import models

class Parc(models.Model):

	code = models.IntegerField("code")
	adresse = models.CharField(("adresse"), max_length=120)
	commentaire = models.TextField("commentaire",blank=True)

