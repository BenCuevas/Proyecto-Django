from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.index, name="index"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('contacto/', views.contacto, name="contacto"),
    path('contacto_forms/', views.contacto_forms, name="contacto_forms"),
    path('carrito/', views.mostrar_carrito, name="carrito"),
    path('productos/', views.mostrar_productos, name="productos"),
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('ers/', views.ers, name="ers"),
    path('agregar_carrito/', views.agregar_carrito, name='agregar_carrito'),
    path('ventas/', views.mostrar_ventas, name='ventas'),
    path('eliminar_ventas/', views.eliminar_ventas, name='eliminar_ventas'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
    path('registro/', views.registro, name='registro'),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('listar-productos/', views.listar_productos, name='listar_productos'),
    path('modificar_producto/<id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar_producto/<id>/', views.eliminar_producto, name='eliminar_producto'),
    
]
