from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm
from .forms import ContatoForm, ProdutoModelForm


def index(requests):
    return render(requests, 'index.html')

def contato(requests):
    form = ContatoForm(requests.POST or None)
    if str(requests.method) == 'POST':
        if form.is_valid():
            """
            nome =  form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem Enviada')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')
            """
            form.send_mail()
            messages.success(requests, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(requests, 'Error ao enviar o e-mail')
    context = {
        'form': form
    }
    return render(requests, 'contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            """
            prod = form.save(commit=False)

            print(f'Nome: {prod.nome}')
            print(f'Preço: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}')
            
            """      
            form.save()
            messages.success(request, 'Produto salvo com sucesso.')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Error ao salvar o produto.')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }
        
    return render(request, 'produto.html', context)