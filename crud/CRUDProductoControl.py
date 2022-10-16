from .ICrud import ICrud
from models.Fertilizante import Fertilizante
from models.ControlPlagas import ControlPlagas


class CRUDProductoControl(ICrud):
    def crear(self, **kwargs):
        if (kwargs['tipo'] == 'ControlPlagas'):
            return ControlPlagas(
                kwargs['registro_ica'],
                kwargs['nombre'],
                kwargs['frec_aplicacion'],
                kwargs['valor'],
                kwargs['periodo_carencia'],
            )

        if (kwargs['tipo'] == 'Fertilizante'):
            return Fertilizante(
                kwargs['registro_ica'],
                kwargs['nombre'],
                kwargs['frec_aplicacion'],
                kwargs['valor'],
                kwargs['fecha_ultima_aplicacion'],
            )

    def mostrar(self, **kwargs):
        pass
