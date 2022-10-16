from models.ProductoControl import ProductoControl


class ControlPlagas(ProductoControl):
    def __init__(self, registro_ica, nombre, frec_aplicacion, valor,
                 periodo_carencia):
        super().__init__(registro_ica, nombre, frec_aplicacion, valor)
        self.__periodo_carencia = periodo_carencia

    def __repr__(self):
        info_producto_control = super().__repr__()
        return f'''
        {info_producto_control}
        periodo carencia: {self.periodo_carencia}
        -------------------------------------'''

    @property
    def periodo_carencia(self):
        return self.__periodo_carencia

    @periodo_carencia.setter
    def periodo_carencia(self, nuevo_periodo):
        self.__periodo_carencia = nuevo_periodo
