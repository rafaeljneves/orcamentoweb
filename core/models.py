from django.db import models

# Create your models here.

class ItemOrcamento(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(
                                'valor',
                                max_digits=9,
                                decimal_places=2,
                                default=0
                               )

    def __str__(self):
        return self.descricao + ' : ' + self.valor


