from datetime import datetime
from ui import mensajes
from crud.CRUDCliente import CRUDCliente
from crud.CRUDPedido import CRUDPedido
from crud.CRUDAntibiotico import CRUDAntibiotico
from crud.CRUDProductoControl import CRUDProductoControl

if __name__ == '__main__':
    crud_cliente = CRUDCliente()
    crud_pedido = CRUDPedido()
    crud_antibiotico = CRUDAntibiotico()
    crud_prod_control = CRUDProductoControl()

    cliente = crud_cliente.crear(nombre='Monachito', cedula='1234567890'),

    base_pedidos = []
    base_antibioticos = [
        crud_antibiotico.crear(
            nombre='antibiotico 1',
            dosis=2,
            tipo_animal='bovino',
            precio=1234.23
        )
    ]
    base_prods_control = [
        crud_prod_control.crear(
            tipo='ControlPlagas',
            registro_ica='abc1234567',
            nombre='Control hongos',
            frec_aplicacion=15,
            valor=1234.23,
            periodo_carencia=30
        ),
        crud_prod_control.crear(
            tipo='Fertilizante',
            registro_ica='abc7654321',
            nombre='Fertilizante Maiz',
            frec_aplicacion=8,
            valor=8765,
            fecha_ultima_aplicacion=datetime.now()
        ),
    ]

    mensajes.mensaje_entrada()
    while True:
        opcion = mensajes.menu_principal()

        # Vender producto
        if (opcion == 1):
            opcion_producto = mensajes.menu_productos()
            fecha_pedido = datetime.now()
            if (opcion_producto == 1):
                index_prod = mensajes.listado_productos(base_antibioticos)
                prod = base_antibioticos[index_prod]
                pedido = crud_pedido.crear(
                    fecha=fecha_pedido, total_compra=prod.precio, producto=prod
                )

            if (opcion_producto == 2):
                index_prod = mensajes.listado_productos(base_prods_control)
                prod = base_prods_control[index_prod]
                pedido = crud_pedido.crear(
                    fecha=fecha_pedido, total_compra=prod.valor, producto=prod
                )

            base_pedidos.append(pedido)

        # Mostrar historial pedidos
        if (opcion == 2):
            mensajes.listado_pedidos(base_pedidos)

            # Salir
        if (opcion == 3):
            mensajes.mensaje_salida()
            break
