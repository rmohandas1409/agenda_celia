from django.db import models
from pyexpat import model


class Ramal(models.Model):
    setor = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    telefone = models.CharField(max_length=10)


class Meta:
    verbose_name_plural = 'ramais'


def __str__(self):
    return self.setor


class Departamento(models.Model):
    setor = models.ForeignKey('Ramal', on_delete=models.CASCADE)


class Meta:
    verbose_name_plural = 'departamentos'


def __str__(self):
    return self.setor
