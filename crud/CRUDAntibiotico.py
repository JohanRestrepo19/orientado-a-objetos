from .ICrud import ICrud
from models.Antibiotico import Antibiotico


class CRUDAntibiotico(ICrud):
    def crear(self, **kwargs):
        return Antibiotico(
            kwargs['nombre'],
            kwargs['dosis'],
            kwargs['tipo_animal'],
            kwargs['precio']
        )

    def mostrar(self, **kwargs):
        pass
