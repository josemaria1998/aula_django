from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpRespanse('pagina Principal')
    return render(request, 'home.html')