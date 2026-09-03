from django.core.validators import MaxValueValidator
from django.db import models


class Libro(models.Model):
    CATEGORIAS = [
        ('ING', 'Ingenieria y Tecnologia'),
        ('CIEN', 'Ciencias Basicas'),
        ('LIT', 'Literatura y Ficcion'),
        ('HIST', 'Historia y Humanidades'),
        ('OTRO', 'Otros'),
    ]

    titulo = models.CharField(max_length=200, verbose_name='Titulo')
    autor = models.CharField(max_length=150, verbose_name='Autor')
    isbn = models.CharField(max_length=20, unique=True, verbose_name='ISBN')
    categoria = models.CharField(max_length=10, choices=CATEGORIAS, default='ING', verbose_name='Categoria')
    año_publicacion = models.PositiveIntegerField(
        verbose_name='Año de Publicacion',
        validators=[MaxValueValidator(2100)],
    )
    cantidad_disponible = models.PositiveIntegerField(default=1, verbose_name='Cantidad Disponible')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['titulo']
        db_table = 'libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return f'{self.titulo} - {self.autor}'
