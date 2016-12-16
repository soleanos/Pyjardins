from django.shortcuts import render
from django.http import HttpResponse
from jardin.models import Parc

def details(request):
	return render(request, 'all.html', {
        'lol': "mdr",
    })
