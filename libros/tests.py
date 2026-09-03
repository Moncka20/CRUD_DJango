from django.test import TestCase
from django.urls import reverse

from .models import Libro


class LibroCrudTests(TestCase):
    def setUp(self):
        self.libro = Libro.objects.create(
            titulo='Libro de prueba', autor='Autor de prueba',
            isbn='978-0000000001', categoria='ING', año_publicacion=2020,
            cantidad_disponible=2,
        )

    def test_listado_muestra_libros(self):
        response = self.client.get(reverse('libros:listar'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Libro de prueba')

    def test_creacion_edicion_y_eliminacion(self):
        response = self.client.post(reverse('libros:crear'), {
            'titulo': 'Nuevo libro', 'autor': 'Nueva autora', 'isbn': '978-0000000002',
            'categoria': 'LIT', 'año_publicacion': 2022, 'cantidad_disponible': 4,
        })
        self.assertRedirects(response, reverse('libros:detalle', args=[2]))
        nuevo = Libro.objects.get(isbn='978-0000000002')

        response = self.client.post(reverse('libros:editar', args=[nuevo.pk]), {
            'titulo': 'Libro actualizado', 'autor': nuevo.autor, 'isbn': nuevo.isbn,
            'categoria': nuevo.categoria, 'año_publicacion': nuevo.año_publicacion,
            'cantidad_disponible': 7,
        })
        self.assertRedirects(response, reverse('libros:detalle', args=[nuevo.pk]))
        nuevo.refresh_from_db()
        self.assertEqual(nuevo.titulo, 'Libro actualizado')
        self.assertEqual(nuevo.cantidad_disponible, 7)

        response = self.client.post(reverse('libros:eliminar', args=[nuevo.pk]))
        self.assertRedirects(response, reverse('libros:listar'))
        self.assertFalse(Libro.objects.filter(pk=nuevo.pk).exists())