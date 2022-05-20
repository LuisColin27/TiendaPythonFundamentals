class Carrito:
    def __init__(self):
        self.carrito = []
        self.total = 0

    def agregar_producto(self, compra):
        self.carrito.append(compra)
        return self.carrito

    def eliminar_producto(self, index):
        self.carrito.pop(index)
        return self.carrito

    def listado_compras(self):
        if(len(self.carrito) > 0):
            print("\nListado de compras")
            for p in self.carrito:
                p.get_detalles_compra()
        else:
            print("\nLa lista de compras se encuentra vacia\n")

    def existe_producto(self, codigo):
        for compra in self.carrito:
            if(compra.codigo == codigo):
                return True
        return False

    def obtener_indice(self, codigo):
        for i in range(0, len(self.carrito)):
            if(self.carrito[i].codigo == codigo):
                return i
        return -1

    def esta_vacio(self):
            if(len(self.carrito)> 0):
                return False
            else:
                return True

    def obtener_producto(self, codigo):
        for compra in self.carrito:
            if(compra.codigo==codigo):
                return compra

    def vaciar_carrito(self):
        self.carrito.clear()

    def obtener_total_neto(self):
        total = 0
        if(len(self.carrito) > 0):
                print("\nListado de compras")
                for p in self.carrito:
                    p.get_detalles_compra()
                    total += p.total
                print("\t\t\t\tTotal:\t"+str(total))
                self.total = total