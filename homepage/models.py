from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria
       

        

class Filme(models.Model):
    filme = models.CharField(max_length=20)
    resenha = models.TextField(max_length=500, blank=True)
    data_criacao = models.DateField(default=timezone.now)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    
    def __str__(self):
        return self.filme
       
    
