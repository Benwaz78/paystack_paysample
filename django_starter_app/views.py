from django.shortcuts import render
from rest_framework import viewsets
from . models import Language, Paradigm, Programer
from .serializers import LanguageSerializer, ParadigmSerializer, ProgramerSerializer
from .forms import PurchaseForm

# Create your views here.

def index(request):
	return render(request, 'django_starter_app/index.html', {'home_key':'Welcome here'})

class LanguageView(viewsets.ModelViewSet):
	queryset = Language.objects.all()
	serializer_class = LanguageSerializer

class ProgrammerView(viewsets.ModelViewSet):
	queryset = Programer.objects.all()
	serializer_class = ProgramerSerializer

class ParadigmView(viewsets.ModelViewSet):
	queryset = Paradigm.objects.all()
	serializer_class = ParadigmSerializer


def purchase(request):
    if request.method == 'POST':
        purch = PurchaseForm(request.POST)
        if purch.is_valid():
            purch.save()
            purch = PurchaseForm()
    else:
        purch = PurchaseForm()
    return render(request, 'django_starter_app/purchase.html', {'p':purch})
