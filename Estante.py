class Estante:
    def __init__(self):
        self.productos = []

    def addProducto(self, producto):
        self.productos.append(producto)
        return self.productos

    def getIndex(self, codigo):
        for i in range(0, len(self.productos)):
            if(self.productos[i].codigoBarras == codigo):
                return i
    
    def eliminarProducto(self,index):
        self.productos.pop(index)
        return self.productos
    
    def getListaProductos(self):
        print("\nListado de producto(s) registrado(s):\n")
        for p in self.productos:
            print(p.toString())
    
    def esta_vacio(self):
        if(len(self.productos)> 0):
            return False
        else:
            return True
        
    def obtener_productos(self, codigo):
        i = self.getIndex(codigo);
        return self.productos[i]