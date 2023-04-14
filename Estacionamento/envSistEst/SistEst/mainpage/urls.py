from django.urls import path
from mainpage.views import home #, sobre, contatos

urlpatterns = [
    path('', home),
    #path('sobre/', sobre),
    #path('contatos/' contatos),
]