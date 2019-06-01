from django.test import TestCase
from .models import ItemOrcamento

class TestItemOrcamento(TestCase):
    def setUp(self):
        self.itemOrcamento = ItemOrcamento.objects.create(
            descricao = 'Caneta esferográfica',
            valor = 2.50
        )

    def test_item_is_created(self):
        item = ItemOrcamento.objects.create(itemOrcamento=self.itemOrcamento)

        self.assertTrue(ItemOrcamento.objects.exists())
