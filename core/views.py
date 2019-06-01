from django.shortcuts import render, redirect
from .models import ItemOrcamento
from .forms import ItemOrcamentoForm
from django.contrib import messages


def index(request):
    if request.method =='POST':
        form = ItemOrcamentoForm(request.POST or None)

        if form.is_valid():
            form.save()
            itens = ItemOrcamento.objects.all
            messages.success(request, ('Item foi adicionado no orçamento.'))
            context = { 'itens': itens}
            return render(request, 'core/index.html', context)
    else:
        itens = ItemOrcamento.objects.all
        context = {'itens': itens}
        return render(request, 'core/index.html', context)


