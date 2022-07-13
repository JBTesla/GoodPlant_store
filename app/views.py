from genericpath import exists
from math import prod
from urllib import response
import requests #NOS PERMITE LEER EL API
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):     
    if created:
       instance.groups.add(Group.objects.get(name='Cliente'))

def must_be_supervisor(user):
   return user.groups.filter(name='Admin').count()
    
def index(request):
    return render(request, 'app/index.html')
@login_required
def perfil(request):
    return render(request, 'app/Usuario/perfilUsuario.html')
@login_required
def agregar_usuario(request):
    datos={
        'form' : usuarioForm()
    }
    if request.method == 'POST':
        formulario= usuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Usuario guardado correctamente!')
    return render(request, 'app/Administrador/agregar_usuarios.html',datos)
 
@login_required
def listar_usuario(request):
    usuarioALL= Usuario.objects.all()
    datos ={'lista_usuario' :usuarioALL,
            } 
    return render(request, 'app/Administrador/listar_usuarios.html',datos)
@login_required
def modificar_usuario(request, rut):
    usuario = Usuario.objects.get(rut=rut)
    datos={
        'form' : usuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario= usuarioForm(request.POST, files=request.FILES,instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario modificado correctamente'
            datos['form'] = formulario
    return render(request,'app/Administrador/modificar_usuarios.html')
@login_required
@permission_required('app.add_usuario')
def eliminar_usuario(request, rut):
    usuario = Usuario.objects.get(rut=rut)
    usuario.delete()

    redirect(to='listar_usuario')
@login_required
def usuario_api(request):
    response = requests.get('http://127.0.0.1:8000/api/usuario/').json()
    datos = {'listaJson' : response}
    return render(request,'app/Administrador/usuario_api.html',datos)
@login_required
def historial(request, id):
    historial_compra= Despacho.objects.filter(usuario=id)
    productos_compra=Items_Despacho.objects.filter(id_user = id)
    datos={'lista_historial':historial_compra,
            'lista_productos':productos_compra}

    return render(request, 'app/Usuario/historialCompras.html',datos)

@login_required
def suscripcion(request, username):

    suscripcion = Suscripcion.objects.filter(username=username)

    datos={'listar_suscripcion':suscripcion,
            'form': suscripcionForm(),
            'usuario' : 0
    }
    susvalida=Suscripcion.objects.filter(username=username).get()
    if Suscripcion.objects.filter(username=username).exists():
        if susvalida.is_suscrito == True:
            datos['usuario'] = 1
        else:
            datos['usuario'] = 0

    if request.method == 'POST':
        if Suscripcion.objects.filter(username=username).exists():
            Suscripcion.objects.filter(username=username).update(is_suscrito= True)
        else:    
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
    suscripcion = Suscripcion.objects.all()

    suscripcion=Suscripcion.objects.get(username=username)
    suscripcion.is_suscrito = False
    suscripcion.save()

    return redirect('/suscripcion/'+username)
@login_required
def seguimiento_despacho(request, id):
    
    historial_compra= Despacho.objects.filter(id=id)
    productos_compra=Items_Despacho.objects.filter(id_pago = id)
    datos={'lista_historial':historial_compra,
            'lista_productos':productos_compra}

    return render(request, 'app/Usuario//seguimiento_despacho.html', datos)
@login_required
def despacho_admin(request):

    if request.method == 'POST':
        despacho= Despacho.objects.get(id=request.POST.get('id'))
        despacho.estado = request.POST.get('selecciona')
        despacho.save()

    despachoAll = Despacho.objects.all()
    datos = {
            'despachoAll':despachoAll,
            'usuario':0
    }
    return render(request, 'app/Administrador/despacho_admin.html', datos)
@login_required
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
                productoA.delete()

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
    }
    lista = carrito
    datos['total']=0

    usuario = request.user.username
    usuario_id = request.user.id
    susvalida=Suscripcion.objects.filter(username=usuario).get()
    if susvalida.is_suscrito == True:
        datos['usuario'] = 1
        for cart in lista:
            datos['totalsub']= round((cart.producto.precio * cart.cantidad +datos['total'])*0.95)
            datos['total']= cart.producto.precio * cart.cantidad + datos['total']
            datos['descuento']=round(datos['total']*0.05)
    else:
        datos['usuario'] = 0
        for cart in lista:
            datos['total']= cart.producto.precio * cart.cantidad + datos['total']
            datos['no_sus']="Debes estar suscrito"
  
    if request.method == 'POST':
        compra= Despacho()
        compra.usuario = usuario_id
        if susvalida.is_suscrito == True:
            compra.total_compra= datos['totalsub']
        else:
            compra.total_compra= datos['total']
        compra.estado ="pago verificado"
        compra.save()
        compraid=compra.id

        for n in carrito:
            despacho = Items_Despacho()

            despacho.cantidad = n.cantidad
            despacho.producto = n.producto
            despacho.id_user = n.user
            despacho.id_pago = compraid
            despacho.save()
        
        carrito.delete()
        datos['mensaje'] = 'pago verificado'
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
            suscrito=Suscripcion()
            suscrito.username = request.POST.get('username')
            suscrito.is_suscrito = False
            suscrito.save()
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #login(request,user)
            #messages.success(request,'Registrado correctamente!')
            #User.groups.add(Empleado)
            #return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'registration/registro.html', datos)

def apiCustom(request):
    response = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes?count=15').json()
    #response2 = requests.get('https://digimon-api.vercel.app/api/digimon').json()
    datos = {'listaJsonLs' : response,
             #'listaJsonDm' : response2
    }

    return render(request, 'app/Usuario/apiCustom.html', datos)