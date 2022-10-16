class Antibiotico:
    def __init__(self, nombre, dosis, tipo_animal, precio):
        self.__nombre = nombre
        self.__dosis = dosis
        self.__tipo_animal = tipo_animal
        self.__precio = precio

    def __repr__(self):
        return f'''
        ---------------------------------------------------
        nombre: {self.nombre}
        dosis: {self.dosis}
        tipo de animal: {self.tipo_animal}
        precio = ${self.precio}
        ---------------------------------------------------
        '''

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def dosis(self):
        return self.__dosis

    @dosis.setter
    def dosis(self, nueva_dosis):
        self.__dosis = nueva_dosis

    @property
    def tipo_animal(self):
        return self.__tipo_animal

    @tipo_animal.setter
    def tipo_animal(self, nuevo_tipo_animal):
        self.__tipo_animal = nuevo_tipo_animal

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio
