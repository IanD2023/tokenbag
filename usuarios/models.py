from django.db import models

class Usuarios(models.Model):
     
     nome = models.CharField(max_length=100,null=True)
     codigo = models.CharField(max_length=100,unique=True)
     senha = models.CharField(max_length=100,null=True)
     cpf = models.CharField(max_length=100,null=True,unique=True)
     loja = models.CharField(max_length=100,null=True)

     def __str__(self):

          self.nome
          self.codigo
          self.senha
          self.loja

          return self    


