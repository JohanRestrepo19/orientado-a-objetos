class Cliente:
    def __init__(self, nombre, cedula) -> None:
        self.__nombre = nombre
        self.__cedula = cedula
        self.__historial = []

    def __repr__(self):
        return f'''
        ----------------------------------
        nombre: {self.nombre}
        cedula: {self.cedula}
        ----------------------------------'''

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, nueva_cedula):
        self.__cedula = nueva_cedula

    @property
    def historial(self):
        return self.__historial

    @historial.setter
    def historial(self, nuevo_pedido):
        self.__historial.append(nuevo_pedido)
