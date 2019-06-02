from django.shortcuts import render, redirect
from .models import ItemOrcamento
from .forms import ItemOrcamentoForm
from django.contrib import messages
from django.db.models import Sum


def index(request):
    if request.method =='POST':
        form = ItemOrcamentoForm(request.POST or None)

        if form.is_valid():
            form.save()
            itens = ItemOrcamento.objects.all
            valor_total = list(ItemOrcamento.objects.aggregate(Sum('valor')).values())[0]
            messages.success(request, ('Item foi adicionado no orçamento.'))
            context = { 'itens': itens,
                        'valor_total': valor_total}


            return render(request, 'core/index.html', context)
    else:
        itens = ItemOrcamento.objects.all
        valor_total = list(ItemOrcamento.objects.aggregate(Sum('valor')).values())[0]


        if valor_total!= None:
           status = None
        else:
           status = 'disabled'
        print('status: ', str(itens))
        context = {'itens': itens,
                   'valor_total': valor_total,
                   'status': status}
        return render(request, 'core/index.html', context)


def excluir(request):
    ItemOrcamento.objects.all().delete()

    context = {'itens': None,
               'valor_total': 0.00,
               'status': 'disabled'}

    return render(request, 'core/index.html', context)

