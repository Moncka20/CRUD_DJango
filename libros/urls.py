from django.urls import path

from . import views

app_name = 'libros'

urlpatterns = [
    path('', views.listar_libros, name='listar'),
    path('nuevo/', views.crear_libro, name='crear'),
    path('<int:pk>/', views.detalle_libro, name='detalle'),
    path('<int:pk>/editar/', views.editar_libro, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_libro, name='eliminar'),
]
