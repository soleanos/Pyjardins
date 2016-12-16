from django.shortcuts import render
from django.http import HttpResponse
from jardin.models import Parc

def catalogue(request):
	mesJardins = Parc.objects.all()
	collectionJardin = list(mesJardins)
	return render(request, 'all.html', {
        'collectionJardin': collectionJardin,
    })
