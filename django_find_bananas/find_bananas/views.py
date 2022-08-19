from django.shortcuts import render
from django.http import HttpResponse
from .create_bananas_images import bananas_of_the_day

def home(request):

  latest_bananas = Bananas.objects.latest('timestamp')

  dico = {
    "round1": {},
    "round2": {},
    "round3": {}
  }


  dico["round1"]["number"] = latest_bananas.nb_bananas_1
  dico["round2"]["number"] = latest_bananas.nb_bananas_2
  dico["round3"]["number"] = latest_bananas.nb_bananas_3
  dico["round1"]["image"] = latest_bananas.image_1
  dico["round2"]["image"] = latest_bananas.image_2
  dico["round3"]["image"] = latest_bananas.image_3

  context = {
    "dico": dico
  }

  return render(request, 'find_bananas/home.html', context)

def about(request):
	return render(request, 'find_bananas/about.html')

# Create your views here.
