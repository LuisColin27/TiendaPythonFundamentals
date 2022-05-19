class Compra:
    
    def __init__(self, codigo, nombre, cantidad, ppu):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.ppu = ppu
        self.total = self.cantidad * self.ppu

    def get_detalles_compra():
        print()