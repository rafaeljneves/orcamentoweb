from django.test import TestCase
from .models import ItemOrcamento

class TestItemOrcamento(TestCase):
    def setUp(self):
        ItemOrcamento.objects.create(descricao = 'Caneta esferográfica', valor = 2.50)

    def test_item_is_created(self):
        item = ItemOrcamento.objects.get(id=1)
        self.assertEqual(item.descricao,"Caneta esferográfica")

    def test_nome_campo_descricao(self):
        item = ItemOrcamento.objects.get(id=1)
        campo_descricao = item._meta.get_field('descricao').verbose_name
        self.assertEquals(campo_descricao, 'descricao')
