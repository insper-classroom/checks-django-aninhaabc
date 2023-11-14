from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('creditos/', views.credito, name='credito'),
    path('anotacoes/<int:note_id>/apagar',views.delete_note, name='delete-note'),
    path('anotacoes/<int:note_id>', views.edit_note, name='edit-note')
]