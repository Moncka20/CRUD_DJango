from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LibroForm
from .models import Libro


def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/libro_list.html', {'libros': libros})


def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/libro_detail.html', {'libro': libro})


def crear_libro(request):
    form = LibroForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        libro = form.save()
        messages.success(request, f'El libro "{libro.titulo}" fue registrado correctamente.')
        return redirect('libros:detalle', pk=libro.pk)
    return render(request, 'libros/libro_form.html', {'form': form, 'titulo': 'Registrar libro'})


def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    form = LibroForm(request.POST or None, instance=libro)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Los datos del libro fueron actualizados.')
        return redirect('libros:detalle', pk=libro.pk)
    return render(request, 'libros/libro_form.html', {'form': form, 'titulo': 'Editar libro', 'libro': libro})


def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        titulo = libro.titulo
        libro.delete()
        messages.success(request, f'El libro "{titulo}" fue eliminado.')
        return redirect('libros:listar')
    return render(request, 'libros/libro_confirm_delete.html', {'libro': libro})
