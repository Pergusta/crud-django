from django.db import models


class Filme(models.Model):
    GENERO_CHOICES = [
        ('ACA', 'Ação'),
        ('COM', 'Comédia'),
        ('DRA', 'Drama'),
        ('TER', 'Terror'),
        ('ANI', 'Animação'),
    ]

    titulo = models.CharField(max_length=150)
    diretor = models.CharField(max_length=100)
    estudio = models.CharField(max_length=100)
    genero = models.CharField(max_length=3, choices=GENERO_CHOICES, default='DRA')
    sinopse = models.TextField(blank=True)
    duracao_minutos = models.IntegerField()
    data_lancamento = models.DateField()
    assistido = models.BooleanField(default=False)

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
