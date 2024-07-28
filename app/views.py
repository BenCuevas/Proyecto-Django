from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Producto
from .forms import ContactoForm, CustomUserCreationForm, ProductoForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def productos(request):
    return render(request, 'productos.html')

def carritoCompra(request):
    return render(request, 'carrito.html')

def ers(request):
    return render(request, 'ers.html')

def contacto(request):
    return render(request, 'contacto.html')

def contacto_forms(request):
    data = {'form':ContactoForm()}
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="contacto guardado"
        else:
            data["form"] = formulario
       
    return render(request, 'contacto_forms.html', data)


def registro(request):
    data ={'form':CustomUserCreationForm()}
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            data["mensaje"]="Usuario registrado"
            return redirect(to="/")
        
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)





# class Producto:
#      def __init__(self, id, nombre, descripcion, stock, precio, foto):
#          self.id = id
#          self.nombre = nombre
#          self.descripcion = descripcion
#          self.stock = stock
#          self.precio = precio
#          self.foto = foto


# Crear lista vacía de productos
lista_productos = []
#lista vacia de carrito
carrito = []
Ventas = []

def mostrar_productos(request):

    # # Producto 1
    # producto1 = Producto(1, "Figura Capitán América 30cm", "Figura Capitán América, tamaño 30cm, colección Marvel Universe", 30, 30000, "img/capitan_america.jpg")
    # lista_productos.append(producto1)

    # # Producto 2
    # producto2 = Producto(2, "Figura Deadpool 25cm", "Figura del Anti-Heroe Deadpool tamaño 25cm de Marvel Universe", 30, 23000, "img/deadpool.jpg")
    # lista_productos.append(producto2)

    # # Producto 3
    # producto3 = Producto(3, "Figura X-Men Wolverine 20cm", "Figura de Wolverine tamaño 20cm Marvel Universe", 20, 20000, "img/wolverine.jpg")
    # lista_productos.append(producto3)
    
    # # Producto 4
    # producto4 = Producto(4, "Figura De X-Men Ciclope 24cm", "Figura de Ciclope tamaño 24cm de Marvel Universe", 30, 22000, "img/ciclope.jpg")
    # lista_productos.append(producto4)
    
    # # Producto 5
    # producto5 = Producto(5, "Figura Ironman 30cm", "Figura de IronMan tamaño 30cm de Marvel Universe", 20, 40000, "img/IronMan.jpg")
    # lista_productos.append(producto5)
    
    # # Producto 6
    # producto6 = Producto(6, "Figura Eva-01 20cm", "Figura de EVA-01 tamaño 20cm de Evangelion", 20, 15000, "img/eva01.jpg")
    # lista_productos.append(producto6)
    
    # # Producto 7
    # producto7 = Producto(7, "Figura Eva-02 20cm", "Figura de EVA-02 tamaño 20cm de Evangelion", 20, 15000, "img/eva02.jpg")
    # lista_productos.append(producto7)
    
    # # Producto 8
    # producto8 = Producto(8, "Figura Dabi 20cm", "Figura de Dabi tamaño 20cm de Boku no Hero Academy", 20, 30000, "img/dabi.jpg")
    # lista_productos.append(producto8)
    
    # # Producto 9
    # producto9 = Producto(9, "Figura De Itachi Uchiha 25cm", "FIgura de Itachi Uchiha tamaño 25cm de Naruto Shippuden", 20, 25000, "img/Itachi.jpg")
    # lista_productos.append(producto9)
    
    # # Producto 10
    # producto10 = Producto(10, "Figura De Flash 25cm", "Figura de Flash tamaño 25cm de DC Universe", 20, 30000, "img/flash.jpg")
    # lista_productos.append(producto10)
    
    # # Producto 11
    # producto11 = Producto(11, "Figura De Superman 30cm", "Figura de SuperMan tamaño 30cm de DC Universe", 20, 40000, "img/superman.jpg")
    # lista_productos.append(producto11)
    
    # # Producto 12
    # producto12 = Producto(12, "Figura De Joker 30cm", "Figura de The Joker tamaño 30cm de DC Universe", 20, 35000, "img/the Joker.jpg")
    # lista_productos.append(producto12)
    
    # # Producto 13
    # producto13 = Producto(13, "Figura De Batman 30cm", "Figura de Batman tamaño 30cm de DC Universe", 20, 40000, "img/muestra-batman.jpg")
    # lista_productos.append(producto13)
    
    # # Producto 14
    # producto14 = Producto(14, "Figura Goku Vs Freezer 25cm", "Figura Goku vs Freezer tamaño 25cm de Dragon Ball Z", 20, 20000, "img/goku_freezer.jpg")
    # lista_productos.append(producto14)
    
    # # Producto 15
    # producto15 = Producto(15, "Figura De Goku 25cm", "Figura de Goku tamaño 25cm de Dragon Ball Z", 20, 20000, "img/muestra-goku.png")
    # lista_productos.append(producto15)
    
    # # Producto 16
    # producto16 = Producto(16, "Figura De Katakuri 25cm", "Figura de Katakuri tamaño 25cm de One Piece", 20, 23000, "img/Katakuri.jpg")
    # lista_productos.append(producto16)
    
    # # Producto 17
    # producto17 = Producto(17, "Figura De Luffy En Barril 15cm", "Figura de Monkey D. Luffy en Barril tamaño 15cm de One Piece", 20, 15000, "img/luffy barril.jpg")
    # lista_productos.append(producto17)
    
    # # Producto 18
    # producto18 = Producto(18, "Figura De Zoro 20cm", "Figura de Roronoa Zoro tamaño 20cm de One Piece", 20, 23000, "img/Roronoa_Zoro.jpg")
    # lista_productos.append(producto18)
    
    # # Producto 19
    # producto19 = Producto(19, "Figura De Vegeta 20cm", "Figura de Vegeta tamaño 20cm de Dragon Ball Z", 20, 25000, "img/vegeta.jpg")
    # lista_productos.append(producto19)

    # # Producto 20
    # producto20 = Producto(20, "Figura De Pain 30cm", "Figura de Pain tamaño 30cm de Naruto Shippuden", 20, 27000, "img/Pain.jpg")
    # lista_productos.append(producto20)
    
    # # Producto 21
    # producto21 = Producto(21, "Figura De Saitama 20cm", "Figura de Saitama tamaño 20cm de OnePunch-Man", 20, 19000, "img/saitama.jpg")
    # lista_productos.append(producto21)
    
    # # Producto 22
    # producto22 = Producto(22, "Figura De Monkey D. Luffy 20cm", "Figura de Monkey D. Luffy tamaño 20cm de One Piece", 20, 25000, "img/Monkey D Luffy.png")
    # lista_productos.append(producto22)
    
    # # Producto 23
    # producto23 = Producto(23, "Figura De Majin Vegeta 20cm", "Figura de Majin Vegeta tamaño 20cm de Dragon Ball Z", 20, 18000, "img/Majin Vegeta.jpg")
    # lista_productos.append(producto23)

    # # Producto 24
    # producto24 = Producto(24, "Figura De Naruto Sannin 30cm", "Figura de Naruto Sannin tamaño 30cm de Naruto Shippuden", 20, 30000, "img/muestra-naruto.png")
    # lista_productos.append(producto24)

    
    # context = {'productos':lista_productos}
    productos = Producto.objects.all()
    context = {'productos':productos}
    return render(request, 'productos.html', context)


def detalle_producto(request, producto_id):
    producto = None
    
    # Buscar el producto con el ID proporcionado en la lista de productos
    for prod in Producto.objects.all():
        if prod.id == producto_id:
            producto = prod
            break
    
    if producto is None:
        # Manejar el caso cuando el producto no se encuentre
        print("Producto no encontrado. ID: ", producto_id)
        return HttpResponse("Producto no encontrado.")
    
    context = {'producto': producto}
    print("Producto encontrado: ", producto.nombre)
    return render(request, 'detalle_producto.html', context)


def agregar_carrito(request):
    if request.method == 'POST':
        producto_id = int(request.POST.get('producto_id'))
        cantidad = int(request.POST.get('cantidad'))
        
        # Buscar el producto en la lista de productos
        producto = None
        for prod in Producto.objects.all():
            if prod.id == producto_id:
                producto = prod
                break
        
        if producto is None:
            # Manejar el caso cuando el producto no se encuentre
            print("Producto no encontrado. ID: ", producto_id)
            return HttpResponse("Producto no encontrado.")
        
        if cantidad > producto.stock:
            # Manejar el caso cuando la cantidad excede el stock disponible
            print("Cantidad excede el stock disponible. Cantidad: ", cantidad)
            return HttpResponse("Cantidad excede el stock disponible.")
        
        # Restar la cantidad del stock
        producto.stock -= cantidad
        producto.save()
        
        # Agregar el producto al carrito
        carrito.append({'producto': producto, 'cantidad': cantidad, 'subtotal': producto.precio * cantidad, 'imagen': producto.imagen})
        
        Ventas.append({'producto': producto, 'cantidad': cantidad})
        # Redirigir a la página del carrito
        return redirect('carrito')

# def mostrar_carrito(request):
#     carrito_productos = []
#     total = 0
#     for item in carrito:
#         producto = item['producto']
#         cantidad = item['cantidad']
#         subtotal = producto.precio * cantidad
#         total += subtotal
#         carrito_productos.append({'producto':producto, 'cantidad':cantidad, 'subtotal':subtotal})
        
#     context = {'carrito': carrito, 'total': total}
#     return render(request, 'carrito.html', context)

def mostrar_carrito(request):
    carrito_productos = []
    total = 0

    if request.method == 'POST' and 'pagar' in request.POST:
        # Procesar el pago y registrar las ventas
        ventas = []
        for item in carrito:
            producto = item['producto']
            cantidad = item['cantidad']
            subtotal = producto.precio * cantidad
            total += subtotal
            carrito_productos.append({'producto':producto, 'cantidad':cantidad, 'subtotal':subtotal})

            # Descontar el stock
            producto.stock -= cantidad
            producto.save()

            # Registrar la venta en la lista Ventas
            venta = {'producto': producto, 'cantidad': cantidad, 'subtotal': subtotal}
            ventas.append(venta)

        # Agregar la lista Ventas al contexto
        context = {'carrito': carrito, 'total': total, 'ventas': ventas}
        return render(request, 'ventas.html', context)

    for item in carrito:
        producto = item['producto']
        cantidad = item['cantidad']
        subtotal = producto.precio * cantidad
        total += subtotal
        carrito_productos.append({'producto':producto, 'cantidad':cantidad, 'subtotal':subtotal})

    context = {'carrito': carrito, 'total': total}
    return render(request, 'carrito.html', context)

def vaciar_carrito(request):
    carrito.clear()
    return redirect('carrito')


def mostrar_ventas(request):
    total_ventas = 0
    ventas = []

    for item in Ventas:
        producto = item['producto']
        cantidad = item['cantidad']
        subtotal = producto.precio * cantidad
        total_ventas += subtotal
        ventas.append({'producto': producto, 'cantidad': cantidad, 'subtotal': subtotal})

    context = {'ventas': ventas, 'total_ventas': total_ventas}
    return render(request, 'ventas.html', context)

def eliminar_ventas(request):
    # Aquí es donde debes eliminar las ventas, en este caso, la lista ventas
    ventas = []  # Vacía la lista de ventas
    return redirect('mostrar_ventas')








# Lista de usuarios para probar el login
# usuarios = [
#     {'username': 'benjamin', 'password': 'ben123'},
#     {'username': 'paolo', 'password': 'paolo123'},
#     {'username': 'alejadnro', 'password': 'ale123'},
#     {'username': 'profesor', 'password': 'profe123'},
#     {'username': 'user', 'password': 'user123'},
# ]

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
        
#         # Buscar el usuario en la lista
#         for i, usuario in enumerate(usuarios):
#             if username == usuario['username'] and password == usuario['password']:
#                 # Guardar el usuario en la sesión
#                 request.session['usuario'] = usuario
#                 # Redirigir al index del proyecto
#                 return redirect('index')
        
#         # Mostrar error si no se encuentra el usuario
#         error = "Usuario o clave incorrectos."
#         return render(request, 'login.html', {'error': error})

#     return render(request, 'login.html')



@login_required
def agregar_producto(request):

    data = {'form':ProductoForm}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario


    return render(request, 'producto/agregar.html', data)

@login_required
def listar_productos(request):
    productos = Producto.objects.all()

    data = {'productos':productos}

    return render(request, 'producto/listar.html', data)

@login_required
def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    data={'form':ProductoForm(instance=producto)}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario

    return render(request, 'producto/modificar.html', data)

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to='listar_productos')
    