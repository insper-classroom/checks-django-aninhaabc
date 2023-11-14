from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Note

def index(request):
    all_notes = Note.objects.all().order_by('created_at')
    # html_response = '<h1>Get-it</h1><ul>'

    # for note in all_notes:
    #     html_response += f'<li>{note.title}</li>'

    # html_response += '</ul>'
    
    return render(request, "notes/index.html" , {'notes' : all_notes})

def credito(request):
    return HttpResponse("<h1>Créditos</h1><p>Sistema web desenvolvido por Ana Beatriz.</p>")
