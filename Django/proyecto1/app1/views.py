from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def pagina(request):
  return render(
    request,
    'app1/main.html'
  )

# Create your views here.
