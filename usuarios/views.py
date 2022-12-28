from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date,timedelta
from .models import Usuarios
from socin import usuarios,extracao,convertmd5,tokendb
from socin import db as Socin

# Create your views here.
def home(request):
    
    usuarios = Usuarios.objects.all()

    return render(request, 'home/index.html',{'usuarios':usuarios})

def autenticar(request):

    Codigo=request.POST.get("codigo")
    Senha=request.POST.get("senha")
    
    user = authenticate(request,username=Codigo, password=Senha)

    if user:

       login(request, user)

       return redirect(senha)

    return render(request, 'home/index.html')

def cadastrar(request):
    
    codigo=request.POST.get("codigo")
    senha=request.POST.get("senha")
    cpf=request.POST.get("cpf")

    if codigo:

        try:

            User.objects.get(username=codigo)
            
            return render(request, 'cadastrar/index.html',{'usuario':"usuario já cadastrado!"})
            
        except User.DoesNotExist:

            try:

                User.objects.get(last_name=cpf)
            
                return render(request, 'cadastrar/index.html',{'cpf':"CPF já cadastrado!"})

            except User.DoesNotExist:

                user = User.objects.create_user(
                username=codigo, last_name=cpf,password=senha,is_staff=False,is_superuser=False)
                user.save()

                return redirect(home)

    return render(request, 'cadastrar/index.html')        

@login_required
def senha(request):
     

     usuario = Socin.listar(request.user.username)
     
     ontem = date.today() - timedelta(1)
     anteontem = date.today() - timedelta(2)

     data = {
        "ontem" : ontem.strftime("%d/%m/%Y"),
        "anteontem" : anteontem.strftime("%d/%m/%Y")
     }

     tokendb.listar(usuario[0][2])

     usuarioSocin=usuarios.UsuarioSocin

     usuarioSocin.login=usuario[0][0]
     usuarioSocin.nome=usuario[0][2]


     return render(request,'token/index.html',{'usuario':usuarioSocin,'data':data})

    