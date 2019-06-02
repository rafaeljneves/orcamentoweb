from django.db import models


class ItemOrcamento(models.Model):
    descricao = models.CharField(max_length=200)
    quantidade = models.IntegerField( default=1)
    valor = models.DecimalField(
                                'valor',
                                max_digits=9,
                                decimal_places=2,
                                default=0
                               )

    def __str__(self):
        return self.descricao + ' : ' + self.valor


