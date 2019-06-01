from django import forms
from .models import ItemOrcamento

class ItemOrcamentoForm(forms.ModelForm):
    class Meta:
        model = ItemOrcamento
        fields= ["descricao", "valor"]