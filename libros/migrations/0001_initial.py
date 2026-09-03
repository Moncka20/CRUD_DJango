from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('autor', models.CharField(max_length=150, verbose_name='Autor')),
                ('isbn', models.CharField(max_length=20, unique=True, verbose_name='ISBN')),
                ('categoria', models.CharField(choices=[('ING', 'Ingenieria y Tecnologia'), ('CIEN', 'Ciencias Basicas'), ('LIT', 'Literatura y Ficcion'), ('HIST', 'Historia y Humanidades'), ('OTRO', 'Otros')], default='ING', max_length=10, verbose_name='Categoria')),
                ('año_publicacion', models.PositiveIntegerField(verbose_name='Año de Publicacion')),
                ('cantidad_disponible', models.PositiveIntegerField(default=1, verbose_name='Cantidad Disponible')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={'verbose_name': 'Libro', 'verbose_name_plural': 'Libros', 'ordering': ['titulo']},
        ),
    ]
