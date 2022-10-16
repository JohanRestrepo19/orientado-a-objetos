import os


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def mensaje_entrada():
    clear()
    print('''
    ----------------------------------------------------------
    Bienvenido al sistema de venta de productos de control.
    ----------------------------------------------------------
    ''')


def menu_principal():
    print('''
    1. Vender un producto.
    2. Mostrar facturas de productos vendidos.
    3. Salir.
    ''')

    opcion = int(input('''
    Ingrese la opcion deseada:
    '''))
    clear()
    return opcion


def menu_productos():
    print('''
    1. Antibiotico
    2. Producto Control
    ''')
    opcion = int(input('''
    Ingrese el tipo de producto que desea
    '''))
    clear()
    return opcion


def listado_productos(lista_prods):
    for index, producto in enumerate(lista_prods):
        print(f'''
        index: {index}
        producto: {producto}''')

    opcion = int(input('''
    Ingrese el index del producto que desea:
    '''))
    clear()
    return opcion


def listado_pedidos(lista_pedidos):
    for pedido in lista_pedidos:
        print(pedido)

    input('Presione enter para continuar: ')
    clear()


def mensaje_salida():
    print('''
    -------------------------------------------------------------
    Gracias por usar el sistema de venta de productos de control.
    -------------------------------------------------------------
    ''')
