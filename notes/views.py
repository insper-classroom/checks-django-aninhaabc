from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Note

def index(request):
    all_notes = Note.objects.all()
    for note in all_notes:
        note.title
    return HttpResponse("<h1>Olá mundo!</h1><p>Este é o app notes de <em>DevLife do Insper</em>.</p><h1>Get-it</h1><ul><li>receita de miojo</li><li>pao doce<li>sorvete com cristais de leite</li><li> iogurte natural</li>homer simpson</li></ul>")

def credito(request):
    return HttpResponse("<h1>Créditos</h1><p>Sistema web desenvolvido por Ana Beatriz.</p>")
