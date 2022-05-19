class Carrito:
    
    def __init__(self):
        self.carrito = []
        
    def agregar_producto(self, compra):
        self.carrito.append(compra)
    
    def eliminar_producto(self, compra):
        self.carrito.remove(compra)
    
    def listado_compras(self):
        print("\nListado de compras")
        for p in self.carrito:
            print(p.codigo+"\t"+p.nombre+"\t"+str(p.cantidad)+"\t"+str(p.ppu)+"\t"+str(p.total))