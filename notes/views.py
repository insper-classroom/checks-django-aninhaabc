from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Note

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        print(f'Titulo={title}\nConteudo={content}\n')

        n = Note(title=title,content=content)
        n.save()

        return redirect('index')
    
    else:
        all_notes = Note.objects.all().order_by('-created_at')
        return render(request, "notes/index.html" , {'notes' : all_notes})

def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')

def edit_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method =='POST':
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.save()
        return redirect('index')
    else:
        return render(request, "notes/index.html",{'note': note})

def credito(request):
    return HttpResponse("<h1>Créditos</h1><p>Sistema web desenvolvido por Ana Beatriz.</p>")
