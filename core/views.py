from django.shortcuts import render, redirect
from .models import ItemOrcamento
from .forms import ItemOrcamentoForm
from django.contrib import messages
from django.db.models import Sum

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods, require_GET

import tempfile

from weasyprint import HTML

CORE_VIEWS = 'core/index.html'


@require_http_methods(["POST", "GET"])  
def index(request):
    '''funcao que acessa a página inicial da aplicacao'''
    if request.method =='POST':
        form = ItemOrcamentoForm(request.POST or None)

        if form.is_valid():
            form.save()
            itens = ItemOrcamento.objects.all
            valor_total = list(ItemOrcamento.objects.aggregate(Sum('valor')).values())[0]
            messages.success(request, ('Item foi adicionado no orçamento.'))
            context = { 'itens': itens,
                        'valor_total': valor_total}


            return render(request, CORE_VIEWS, context)
    else:
        itens = ItemOrcamento.objects.all
        valor_total = list(ItemOrcamento.objects.aggregate(Sum('valor')).values())[0]


        if valor_total!= None:
           status = None
        else:
           status = 'disabled'

        context = {'itens': itens,
                   'valor_total': valor_total,
                   'status': status}
        return render(request, CORE_VIEWS, context)


@require_http_methods(["POST"])  
def excluir(request):
    '''exclui item de orcamento da lista'''
    ItemOrcamento.objects.all().delete()

    context = {'itens': None,
               'valor_total': 0.00,
               'status': 'disabled'}

    return render(request, CORE_VIEWS, context)



@require_http_methods(["GET"])  
def html_to_pdf_view(request):
    ''' converte html para pdf --> html.write_pdf(target='/tmp/mypdf.pdf')    fs = FileSystemStorage('/tmp') '''

    try:
        itens = ItemOrcamento.objects.all
        valor_total = list(ItemOrcamento.objects.aggregate(Sum('valor')).values())[0]

        if valor_total != None:
            status = None
        else:
            status = 'disabled'

        context = {'itens': itens,
                   'valor_total': valor_total,
                   'status': status
                  }

        html_string = render_to_string('core/orcamento_template.html', context)
        html = HTML(string=html_string)

        

        
        with tempfile.TemporaryDirectory() as tmpdirname:
            target_final = '/' + tmpdirname + '/mypdf.pdf'
            html.write_pdf(target=target_final);

        
            fs = FileSystemStorage(tmpdirname)
            with fs.open('mypdf.pdf') as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
            return response

    except Exception as e:
        print(e)

    
