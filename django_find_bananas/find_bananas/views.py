from django.shortcuts import render
from django.http import HttpResponse
from .create_bananas_images import bananas_of_the_day

def home(request):
	#if (request.GET.get('play')):
	dico = bananas_of_the_day()
	context = {
		"dico": dico
	}
	return render(request, 'find_bananas/home.html', context)

def about(request):
	return render(request, 'find_bananas/about.html')

# Create your views here.
