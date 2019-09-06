from django.db import models

# Create your models here.

class Musica(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome'
    )
    artista = models.CharField(
        max_length=50,
        verbose_name='Artista'
    )
    genero_musica = models.CharField(
        max_length=50,
        verbose_name='Genero musical'
    )
    link = models.CharField(
        max_length=50,
        verbose_name='Link da musica'
    )
    def __str__(self):
        return self.nome + '-' + self.artista 