from .ICrud import ICrud
from models.Pedido import Pedido


class CRUDPedido (ICrud):
    def crear(self, **kwargs):
        return Pedido(
            kwargs['fecha'],
            kwargs['total_compra'],
            kwargs['producto']
        )

    def mostrar(self, **kwargs):
        pass
