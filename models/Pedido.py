
class Pedido:
    def __init__(self, fecha, total_compra, producto) -> None:
        self.__fecha = fecha
        self.__total_compra = total_compra
        self.__producto = producto

    def __repr__(self):
        return f'''
        <-------------------------------------------------------->
        fecha pedido: {self.fecha}
        total compra: {self.total_compra}
        producto: {self.producto}
        <-------------------------------------------------------->
        '''

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nuevo_nombre):
        self.__fecha = nuevo_nombre

    @property
    def total_compra(self):
        return self.__total_compra

    @total_compra.setter
    def total_compra(self, nueva_cedula):
        self.__total_compra = nueva_cedula

    @property
    def producto(self):
        return self.__producto
