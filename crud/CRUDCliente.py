from .ICrud import ICrud
from models.Cliente import Cliente


class CRUDCliente(ICrud):

    def crear(self, **kwargs):
        return Cliente(kwargs['nombre'], kwargs['cedula'])

    def mostrar(self, **kwargs):
        pass
