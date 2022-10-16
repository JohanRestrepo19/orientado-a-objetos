from models.ProductoControl import ProductoControl


class Fertilizante(ProductoControl):
    def __init__(self, registro_ica, nombre, frec_aplicacion, valor,
                 fecha_ultima_aplicacion):
        super().__init__(registro_ica, nombre, frec_aplicacion, valor)
        self.__fecha_ultima_aplicacion = fecha_ultima_aplicacion

    def __repr__(self):
        info_producto_control = super().__repr__()
        return f'''
        {info_producto_control}
        fecha ultima aplicacion: {self.fecha_ultima_aplicacion}
        -------------------------------------'''

    @property
    def fecha_ultima_aplicacion(self):
        return self.__fecha_ultima_aplicacion

    @fecha_ultima_aplicacion.setter
    def fecha_ultima_aplicacion(self, nueva_fecha):
        self.fecha_ultima_aplicacion = nueva_fecha
