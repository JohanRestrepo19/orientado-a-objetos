class ProductoControl:
    def __init__(self, registro_ica, nombre, frec_aplicacion, valor):
        self.__registro_ica = registro_ica
        self.__nombre = nombre
        self.__frec_aplicacion = frec_aplicacion
        self.__valor = valor

    def __repr__(self):
        return f'''
        -------------------------------------
        registro_ica: {self.registro_ica}
        nombre: {self.nombre}
        frecuencia aplicación: {self.frec_aplicacion} dias
        valor: ${self.valor}'''

    @property
    def registro_ica(self):
        return self.__registro_ica

    @registro_ica.setter
    def registro_ica(self, nuevo_registro):
        self.__registro_ica = nuevo_registro

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def frec_aplicacion(self):
        return self.__frec_aplicacion

    @frec_aplicacion.setter
    def frec_aplicacion(self, nueva_frec_aplicacion):
        self.__frec_aplicacion = nueva_frec_aplicacion

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nuevo_valor):
        self.__valor = nuevo_valor
