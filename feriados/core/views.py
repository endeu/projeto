##from django.http import HttpResponse
##def feriado(request):

##    return HttpResponse("Não é feriado.")

from django.shortcuts import render
def feriado(request):
      return render(request, 'feriado.html')