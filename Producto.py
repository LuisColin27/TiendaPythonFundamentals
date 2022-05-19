class Producto:
    
    def __init__(self, codigoBarras, nombre, precio, cantidad):
        self.codigoBarras = codigoBarras;
        self.nombre = nombre;
        self.precio = precio;
        self.cantidad = cantidad;

    def toString(self):
        return "Codigo de Barras: "+self.codigoBarras+"\nNombre: "+self.nombre+"\nPrecio: "+str(self.precio)+"\nCantidad: "+str(self.cantidad)+"\n"
