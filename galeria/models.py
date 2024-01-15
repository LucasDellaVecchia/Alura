from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    OPCOES_CAT = [
        ("ESTRELA", "Estrela"),
        ("NEBULOSA", "Nebulosa"),
        ("PLANETA", "Planeta"),
        ("PLANETA ANAO", "Planeta Anao"),
        ("COMETA", "Cometa"),
        ("GALAXIA", "Galaxia"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CAT, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    data_publica = models.DateTimeField(default=datetime.now, blank=False)
    publica = models.BooleanField(default=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
