from django.shortcuts import render
from django.http import HttpResponse
from jardin.models import Parc
from django.shortcuts import get_object_or_404
from jardin.forms import jardinForm

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

def modif(request,code):
	jardinAModifier = Parc.objects.get(code=code)
	form = jardinForm(instance=jardinAModifier)

	if request.method == 'GET':
		monJardin = get_object_or_404(Parc, code=code)
		return render(request, 'update.html', {
			'jardin':monJardin,
			'form':form, 
		})
	elif request.method == 'POST':
		f = jardinForm(request.POST)
		updateJardin = f.save()

  
