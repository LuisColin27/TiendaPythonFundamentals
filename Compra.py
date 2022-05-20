class Compra:
    
    def __init__(self, codigo, nombre, cantidad, ppu):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.ppu = ppu
        self.total = self.cantidad * self.ppu

    def get_detalles_compra(self):
        print(self.codigo+"\t"+self.nombre+"\t"+str(self.cantidad)+"\t"+str(self.ppu)+"\t"+str(self.total))