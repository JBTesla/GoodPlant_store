import re
from.forms import *
from.models import *
from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def perfil(request):
    return render(request, 'app/Usuario/perfilUsuario.html')

def perfil_admin(request):
    return render(request, 'app/Administrador/perfilAdmin.html')

def historial(request):
    return render(request, 'app/Usuario/historialCompras.html')

def suscripcion(request):
    return render(request, 'app/Usuario/suscripcion.html')

def seguimiento1(request):
    return render(request, 'app/Usuario/seguimientoDespacho1.html')

def seguimiento2(request):
    return render(request, 'app/Usuario/seguimientoDespacho2.html')

def seguimiento3(request):
    return render(request, 'app/Usuario/seguimientoDespacho3.html')

def productos(request):
    productoALL= Producto.objects.all()
    datos ={'lista_Productos' :productoALL}

    if request.method == 'POST':
        tipo= TipoProducto()
        tipo.tipo =request.POST.get('tipo_producto')

        producto = Producto()
        producto.codigo = request.POST.get('codigo_producto')
        producto.nombre = request.POST.get('nombre_producto')
        producto.marca = request.POST.get('marca_producto')
        producto.precio = request.POST.get('precio_producto')
        producto.descripcion = request.POST.get('descripcion_producto')
        producto.stock = request.POST.get('stock_producto')
        producto.imagen = request.POST.get('imagen_producto')
        producto.tipo = tipo

        carrito = Items_Carrito()
        carrito.codigo = producto
        carrito.save()
        
    return render(request, 'app/Usuario/productos.html', datos)

def agregar_productos(request):
    datos={
        'form' : productoForm()
    }
    if request.method == 'POST':
        formulario= productoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto guardado correctamente'
    return render(request, 'app/Administrador/agregar_productos.html',datos)

def modificar_productos(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos={
        'form' : productoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario= productoForm(request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente'
            datos['form'] = formulario

    return render(request, 'app/Administrador/modificar_productos.html',datos)

def eliminar_productos(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="list_products")

def listar_productos(request):
    productoALL= Producto.objects.all()
    datos ={
        'listarproductos' :productoALL
    }
    return render(request, 'app/Administrador/listar_productos.html',datos)

def agregar_usuarios(request):
    datos={
        'form2' : usuarioForm()
    }
    if request.method == 'POST':
        formulario= usuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'usuario agregado correctamente'
    return render(request, 'app/Administrador/agregar_usuarios.html',datos)


def modificar_usuarios(request, rut):
    usuario = Usuario.objects.get(rut=rut)
    datos={
        'form2' : usuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario= usuarioForm(request.POST, files=request.FILES,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario modificado correctamente'
            datos['form2'] = formulario

    return render(request, 'app/Administrador/modificar_usuarios.html',datos)

def eliminar_usuario(request, rut):
    usuario = Usuario.objects.get(rut=rut)
    usuario.delete()

    return redirect(to="list_users")

def listar_usuarios(request):
    usuariosALL= Usuario.objects.all()
    datos={
        'listarusuarios' :usuariosALL
    }
    return render(request, 'app/Administrador/listar_usuarios.html',datos)

def carrito(request):
    carrito= Items_Carrito.objects.all()
    datos={ 'listar_carrito' :carrito }

    return render(request, 'app/Usuario/carrito.html', datos)

def pago_recibido(request):
    carrito = Items_Carrito.objects.all()
    carrito.delete()

    return render(request, 'app/Usuario/success.html')

def eliminar_item(request):
    carrito = Items_Carrito.objects.all()
    carrito.delete()

    return redirect(to="cart")