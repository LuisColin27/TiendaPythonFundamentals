from math import prod


class Estante:
    def __init__(self):
        self.productos = []

    def add_producto(self, producto):
        self.productos.append(producto)
        return self.productos

    def get_index(self, codigo):
        for i in range(0, len(self.productos)):
            if(self.productos[i].codigoBarras == codigo):
                return i
        return -1
    
    def eliminar_producto(self,index):
        self.productos.pop(index)
        return self.productos
    
    def listar_productos(self):
        print("\nListado de producto(s) registrado(s):\n")
        for p in self.productos:
            print(p.toString())
    
    def esta_vacio(self):
        if(len(self.productos)> 0):
            return False
        else:
            return True 
        
    def obtener_productos(self, codigo):
        i = self.get_index(codigo);
        return self.productos[i]

    def reducir_venta(self, carrito):
        for compra in carrito.carrito:
            for producto in self.productos:
                if(producto.codigoBarras ==  compra.codigo):
                    producto.cantidad -= compra.cantidad