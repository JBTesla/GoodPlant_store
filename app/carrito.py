from turtle import st


class Carrito:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito= self.session["carrito"] = {}
        else:
            self.carrito = carrito

    def add(self, producto):
        id= str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre":producto.nombre,
                "cantidad":producto.cantidad,
                "precio":producto.precio,
                "imagen":producto.imagen.url
            }
        else:
            self.carrito[id]["cantidad"] +=producto.cantidad
            self.carrito[id]["precio"] +=producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"]= self.carrito
        self.session.modified = True
    
    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"]-= producto.cantidad
            self.carrito[id]["precio"]-= producto.precio
            if self.carrito[id]["cantidad"] <=0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["cart"] = {}
        self.session.modified = True
