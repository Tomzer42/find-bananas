from django.shortcuts import render
from django.http import HttpResponse
from bananas_updater.create_bananas import bananas_of_the_day
from find_bananas.models import Bananas
from datetime import datetime

def home(request):
  print(Bananas.objects.count())
  print(Bananas.objects.latest('timestamp'))
  if Bananas.objects.count() == 0 :
    bananas_of_the_day(True)

  latest_bananas = Bananas.objects.latest('timestamp')

  dico = {
    "round1": {},
    "round2": {},
    "round3": {}
  }


  dico["round1"]["number"] = latest_bananas.nb_bananas_1
  dico["round2"]["number"] = latest_bananas.nb_bananas_2
  dico["round3"]["number"] = latest_bananas.nb_bananas_3
  dico["timestamp"] = str(int(datetime.timestamp(datetime.now())))
  print("Round 1 :", dico["round1"]["number"])
  print("Round 2 :", dico["round2"]["number"])
  print("Round 3 :", dico["round3"]["number"])


  context = {
    "dico": dico
  }

  return render(request, 'find_bananas/home.html', context)

def about(request):
	return render(request, 'find_bananas/about.html')

# Create your views here.
