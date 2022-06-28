from genericpath import exists
from math import prod
from urllib import response
import requests #NOS PERMITE LEER EL API
from django.contrib.auth.models import User
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
def historial(request, id):
    historial_compra= Despacho.objects.filter(usuario=id)
    datos={'lista_historial':historial_compra}
    return render(request, 'app/Usuario/historialCompras.html',datos)

@login_required
def suscripcion(request):

    suscripcion = Suscripcion.objects.all()

    datos={'listar_suscripcion':suscripcion,
            'form': suscripcionForm(),
            'usuario' : 0
    }
    usuario= request.user.username
    if Suscripcion.objects.filter(username=usuario).exists():
        datos['usuario'] = 1

    if request.method == 'POST':
        suscrito=Suscripcion()
        suscrito.username = request.POST.get('username')
        suscrito.is_suscrito = True
        suscrito.save()

    return render(request, 'app/Usuario/suscripcion.html',datos)

def listar_suscripcion(request):
    suscrito = Suscripcion.objects.all()
    datos={'listar_suscripcion':suscrito}

    return render(request, 'app/Usuario/suscripcion.html', datos)

@login_required
def eliminar_suscripcion(request, username):
    suscripcion=Suscripcion.objects.get(username=username)
    suscripcion.delete()

    return redirect(to="suscribe")
@login_required
def seguimiento_despacho(request):
    
    datos={ }

    if request.method == 'POST':

        producto = Producto()
        producto.nombre = request.POST.get('nombre_producto')
        producto.precio = request.POST.get('precio_producto')
        producto.descripcion = request.POST.get('codigo_producto')
        producto.cantidad = request.POST.get('cantidad_producto')
        estado = request.POST.get('estado_producto')
        producto.imagen = request.POST.get('imagen_producto')
        print(producto)
        datos['producto']= producto
        datos['estado'] = estado



    return render(request, 'app/Usuario//seguimiento_despacho.html', datos)

def despacho_admin(request):

    if request.method == 'POST':
        despacho= Despacho.objects.get(codigo=request.POST.get('codigo_producto'))
        despacho.estado = request.POST.get('selecciona')
        despacho.save()

    despachoAll = Despacho.objects.all()
    datos = {
            'despachoAll':despachoAll,
            'usuario':0
    }
    return render(request, 'app/Administrador/despacho_admin.html', datos)

def eliminar_despacho(request, codigo):
    despacho = Despacho.objects.get(codigo=codigo)
    despacho.delete()

    return redirect(to="despacho_admin")
@login_required    
def productosApi(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()
    datos = {'listaJson' : response}

    return render(request, 'app/Usuario/productosApi.html', datos)
    
@login_required
def productos(request):
    cid = request.user.id
    carritoAll= Items_Carrito.objects.all()
    productoALL= Producto.objects.all()
    datos ={'lista_Productos' :productoALL,
            'carro': carritoAll,
             'id': cid,
            } 

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
        carrito.user = cid
        carrito.cantidad = 0
        var_estado = True
        if Items_Carrito.objects.filter(producto=request.POST.get('codigo_producto')).exists():
            for n in carritoAll:
                if n.producto.nombre == producto.nombre:
                    n.cantidad = n.cantidad + 1
                    n.save()
                    var_estado = False 
        else:
            carrito.producto = producto
            carrito.cantidad = 1
            carrito.save()
            var_estado = False
            
        if var_estado == True:
            carrito.producto = producto
            carrito.cantidad = 1
            carrito.save()
        
        
        codigo = request.POST.get('codigo_producto')
        productoA = Producto.objects.get(codigo=codigo)
        if productoA == Producto.objects.get(codigo=codigo):
            if productoA.stock > 0:
                productoA.stock = productoA.stock -1
                productoA.save()
            else:
                producto.stock == 0
                productoA.save()

    return render(request, 'app/Usuario/productos.html', datos, )

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
        'listarproductos' :productoALL,
    }
    return render(request, 'app/Administrador/listar_productos.html',datos)
@login_required
def carrito(request, id):
    carrito= Items_Carrito.objects.filter(user=id)

    datos={ 'listar_carrito' :carrito,
            'usuario': 0,
            'usr': id
    }
    lista = carrito
    datos['total']=0

    usuario = request.user.username
    if Suscripcion.objects.filter(username=usuario).exists():
        datos['usuario'] = 1
        for cart in lista:
            datos['totalsub']= round((cart.producto.precio * cart.cantidad +datos['total'])*0.95)
            datos['total']= cart.producto.precio * cart.cantidad + datos['total']
            datos['descuento']=round(datos['total']*0.05)
    else:
        for cart in lista:
            datos['total']= cart.producto.precio * cart.cantidad + datos['total']
            datos['no_sus']="Debes estar suscrito"
    if request.method == 'POST':
        for n in carrito:
            despacho = Despacho()

            despacho.codigo = n.id
            despacho.cantidad = n.cantidad
            despacho.producto = n.producto
            despacho.usuario = n.user
            despacho.estado = "Pago recibido"
            despacho.save()

        carrito.delete()
        datos['mensaje'] = 'pagado'
        messages.success(request,'Pago realizado con exito')

    return render(request, 'app/Usuario/carrito.html', datos)

@login_required
def pago_recibido(request):
    carrito = Items_Carrito.objects.all()
    carrito.delete()

    return render(request, 'app/Usuario/success.html')

def limpiar_carrito(request):
    carrito = Items_Carrito.objects.all()
    carrito.delete()

    return redirect(to="cart")

def eliminar_item(request , codigo):
    carritoA = Items_Carrito.objects.get(producto_id=codigo)
    usuario= str(carritoA.user)
    

    productoA = Producto.objects.get(codigo=codigo)
    productoA.stock += carritoA.cantidad
    productoA.save()
    
    carritoA.delete()

    return redirect('/carrito/'+usuario)

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
            #messages.success(request,'Registrado correctamente!')
            #User.groups.add(Empleado)
            #return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'registration/registro.html', datos)

def apiCustom(request):
    response = requests.get('https://rickandmortyapi.com/api/character?page=2').json()
    response2 = requests.get('https://digimon-api.vercel.app/api/digimon').json()
    datos = {'listaJsonRM' : response,
             'listaJsonDm' : response2
    }

    return render(request, 'app/Usuario/apiCustom.html', datos)