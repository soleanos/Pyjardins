from django.shortcuts import render
from django.http import HttpResponse
from jardin.models import Parc
from django.shortcuts import get_object_or_404

def index(request):
	return render(request, 'home.html', {
        'welcome': "Bienvenue sur le super site de jardins",
    })

def catalogue(request):
	mesJardins = Parc.objects.all()
	collectionJardin =list(mesJardins)
	return render(request, 'all.html', {
        'collectionJardin': collectionJardin,
    })
    

def details(request,code):
	monJardin = get_object_or_404(Parc, code=code)
	return render(request, 'details.html', {
        'jardin': monJardin,
    })

  
