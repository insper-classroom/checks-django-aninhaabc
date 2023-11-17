from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Note
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        author = request.user

        n = Note(title=title,content=content,author=author)
        n.save()

        return redirect('index')
    
    else:
        all_notes = Note.objects.all().order_by('-created_at')
        usuario_selecionado = request.user
        anotacoes_do_usuario = Note.objects.filter(author=usuario_selecionado).order_by('-created_at')
        return render(request, "notes/index.html" , {'notes' : anotacoes_do_usuario})

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
