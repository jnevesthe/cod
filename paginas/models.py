from django.db import models

class Inf(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.titulo
