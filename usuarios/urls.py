from django.urls import path
from .views import home, autenticar,cadastrar,senha


urlpatterns = [

    path('', home,name="home"),
    path('autenticar/', autenticar,name="autenticar"),
    path('criar-acesso/', cadastrar,name="criaracesso"),
    path('senha/', senha,name="senha"),

]
