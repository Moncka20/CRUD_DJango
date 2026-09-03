from django.core.management.base import BaseCommand

from libros.models import Libro


class Command(BaseCommand):
    help = 'Carga los cinco libros de prueba de la biblioteca.'

    def handle(self, *args, **options):
        books = [
            ('Clean Code', 'Robert C. Martin', '978-0132350884', 'ING', 2008, 4),
            ('Design Patterns', 'Erich Gamma et al.', '978-0201633610', 'ING', 1994, 2),
            ('Cien Anos de Soledad', 'Gabriel Garcia Marquez', '978-0307474728', 'LIT', 1967, 5),
            ('Introduction to Algorithms', 'Thomas H. Cormen', '978-0262033848', 'CIEN', 2009, 3),
            ('Breve Historia del Tiempo', 'Stephen Hawking', '978-8497596725', 'CIEN', 1988, 6),
        ]
        for book in books:
            Libro.objects.update_or_create(isbn=book[2], defaults={
                'titulo': book[0], 'autor': book[1], 'categoria': book[3],
                'año_publicacion': book[4], 'cantidad_disponible': book[5],
            })
        self.stdout.write(self.style.SUCCESS('Se cargaron 5 libros de prueba.'))
