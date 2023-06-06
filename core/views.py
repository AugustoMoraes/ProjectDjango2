from django.shortcuts import render

def index(requests):
    return render(requests, 'index.html')

def contato(requests):
    return render(requests, 'contato.html')

def produto(requests):
    return render(requests, 'produto.html')