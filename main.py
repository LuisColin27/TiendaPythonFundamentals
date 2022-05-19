from Producto import *
from Estante import *
from Compra import *
from Carrito import *

def registrarProducto(estante):
        while True:
            codigo = input('Ingrese el codigo de barras:\n')
            nombre = input('Ingrese el nombre del producto:\n')
            precio = float(input('Ingrese el precio del producto:\n'))
            unidades = int(input('Ingrese la unidades disponibles:\n'))

            prod = Producto(codigo, nombre, precio, unidades)
            estante.addProducto(prod)

            r = input("¿Desea registrar otro producto?(S/N)\n")
            if (r == 'N'):
                return estante
            continue

def eliminarProducto(estante):
        while True:
            estante.getListaProductos()
            if(not estante.esta_vacio()):
                codigo = input("Ingrese el codigo de barras del producto o presione Q para cancelar:\n")
                if(codigo != 'Q'):
                    indice = estante.getIndex(codigo)
                    estante.eliminarProducto(indice)
                    r = input("¿Desea eliminar otro producto? (S/N)")
                    if(r == 'S'):
                        continue
                    else:
                        return estante
                else:
                    return estante
            else:
                print("No puede eliminar mas productos. Ya que la lista se encuentra vacia")
                break

def agregarCompra(estante, carrito):
    while True:
        if(not estante.esta_vacio()):
            estante.getListaProductos()
            cod = input("Ingrese el codigo de barras del producto\n")
            producto = estante.obtener_productos(cod)
            cantidades = int(input("Ingrese las unidades a comprar:\n"))
            compra = Compra(producto.codigoBarras, producto.nombre, cantidades ,producto.precio)
            carrito.agregar_producto(compra)
            
            carrito.listado_compras();
        else:
            break

estante = Estante()

while True:
    print("\nDel siguente menú seleccione la opción que mas se adpate a sus necesidades:")
    print("1. Registrar un producto\n2. Eliminar un producto\n3. Realizar una compra\nQ. Salir\n")
    opcion = input("Seleccione una opción:\n")
    
    if(opcion =='1'):
        estante = registrarProducto(estante)
        continue
    elif(opcion =='2'):
        estante = eliminarProducto(estante)
        continue
    elif(opcion == '3'):
        while True:
            carrito = Carrito()
            print("\nMenú de compras:")
            op = input("1. Seleccionar producto\n2. Quitar producto de la lista\nQ. Salir")
            if(op == '1'):
                agregarCompra(estante, carrito)
                continue
            elif(op == 'Q'):
                break
        continue
    elif(opcion =='Q'):
        break
    else:
        print("Ha seleccionado una opción no valida")
