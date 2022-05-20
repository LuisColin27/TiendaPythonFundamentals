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
            estante.add_producto(prod)

            r = input("¿Desea registrar otro producto?(S/N)\n")
            if (r == 'N'):
                return estante
            continue

def eliminarProducto(estante):
        while True:
            estante.listar_productos()
            if(not estante.esta_vacio()):
                codigo = input("Ingrese el codigo de barras del producto o presione Q para cancelar:\n")
                if(codigo != 'Q'):
                    indice = estante.get_index(codigo)
                    estante.eliminar_producto(indice)
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
            estante.listar_productos()
            cod = input("Ingrese el codigo de barras del producto o presione Q para Salir\n")
            if(cod != 'Q'):
                producto = estante.obtener_productos(cod)
                cantidades = int(input("Ingrese las unidades a comprar:\n"))
                compra = Compra(producto.codigoBarras, producto.nombre, cantidades ,producto.precio)
                carrito.agregar_producto(compra)
                carrito.listado_compras();
                return carrito
            else:
                break
        else:
            break

def quitarCompra(carrito):
    while True:
        if(not carrito.esta_vacio()):
            codigo = input("Ingrese el codigo del producto a eliminar de la compra o presione Q para salir\n")
            if(codigo != 'Q'):
                compra = carrito.obtener_indice(codigo)
                carrito.carrito = carrito.eliminar_producto(compra)
                r = input("¿Desea eliminar otro producto? (S/N)")
                if(r != 'S'):
                    return carrito
                else:
                    continue
            else:
                break
        else:
            print("La lista de compras se encuentra vacia, no puede eliminar nada más. ")
            break

def finalizar_compra(carrito):
    if(not carrito.esta_vacio()):
        carrito.obtener_total_neto()
        while True:
            r = input("1. Pagar\n2. Cancerlar y regresar a comprar\n")
            if(r=='1'):
                while True:
                    total = float(input("Ingrese la cantidad de dinero\n"))
                    if(total >= carrito.total):
                        print("Su cambio es: "+str(total - carrito.total))
                        print("Gracias por su compra")
                        return True
                    else:
                        print("El monto ingresado es menor a la cantidad a pagar")
                        continue
            elif(r=='2'):
                return False
    else:
        print("La lista de compras se encuentra vacia. No podemos procesar su solicitud")

estante = Estante()
carrito = Carrito()

while True:
    print("\nDel siguente menú seleccione la opción que mas se adpate a sus necesidades:")
    print("1. Registrar un producto\n2. Eliminar un producto\n3. Realizar una compra\n4. Mostrar productos registrados\nQ. Salir\n")
    opcion = input("Seleccione una opción:\n")
    if(opcion =='1'):
        estante = registrarProducto(estante)
        continue
    elif(opcion =='2'):
        estante = eliminarProducto(estante)
        continue
    elif(opcion == '3'):
        while True:
            print("\nMenú de compras:")
            op = input("1. Seleccionar producto\n2. Quitar producto de la lista\n3. Mostrar ticket\n4. Finalizar compra\nQ. Salir\n")
            if(op == '1'):
                carrito = agregarCompra(estante, carrito)
                continue
            elif(op == '2'):
                carrito = quitarCompra(carrito)
                continue
            elif(op == '3'):
                carrito.listado_compras()
                continue
            elif(op == '4'):
                if(finalizar_compra(carrito)):
                    estante.reducir_venta(carrito)
                    carrito.vaciar_carrito()
                    break
                else:
                    continue
            elif(op == 'Q'):
                break
        continue
    elif(opcion == '4'):
        estante.listar_productos()
        continue
    elif(opcion =='Q'):
        break
    else:
        print("Ha seleccionado una opción no valida")
