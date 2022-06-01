from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'app/index.html')
@login_required
def perfil(request):
    return render(request, 'app/Usuario/perfilUsuario.html')
@login_required
def historial(request):
    return render(request, 'app/Usuario/historialCompras.html')
@login_required
def suscripcion(request):
    return render(request, 'app/Usuario/suscripcion.html')
@login_required
def seguimiento1(request):
    return render(request, 'app/Usuario/seguimientoDespacho1.html')
@login_required
def seguimiento2(request):
    return render(request, 'app/Usuario/seguimientoDespacho2.html')
@login_required
def seguimiento3(request):
    return render(request, 'app/Usuario/seguimientoDespacho3.html')
@login_required
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

@login_required
@permission_required('app.add_producto')
def agregar_productos(request):
    datos={
        'form' : productoForm()
    }
    if request.method == 'POST':
        formulario= productoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
            
    return render(request, 'app/Administrador/agregar_productos.html',datos)
@login_required
@permission_required('app.change_producto')
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
@login_required
@permission_required('app.delete_producto')
def eliminar_productos(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="list_products")
@login_required
@permission_required('app.add_producto')
def listar_productos(request):
    productoALL= Producto.objects.all()
    datos ={
        'listarproductos' :productoALL
    }
    return render(request, 'app/Administrador/listar_productos.html',datos)
@login_required
def carrito(request):
    carrito= Items_Carrito.objects.all()
    datos={ 'listar_carrito' :carrito }

    return render(request, 'app/Usuario/carrito.html', datos)
@login_required
def pago_recibido(request):
    carrito = Items_Carrito.objects.all()
    carrito.delete()

    return render(request, 'app/Usuario/success.html')

def eliminar_item(request):
    carrito = Items_Carrito.objects.all()
    carrito.delete()

    return redirect(to="cart")

def register(request):
    datos = {
        'form' : FormularioUserResgistro()
    }
    if request.method == 'POST':
        formulario = FormularioUserResgistro(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #login(request,user)
            messages.success(request,'Registrado correctamente!')
            #return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'registration/registro.html', datos)