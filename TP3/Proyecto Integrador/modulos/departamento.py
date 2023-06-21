class Departamento():
    def __init__(self, nombre, jefe):
        self.__jefe=jefe
        self.__reclamos_depto=[]
        self.__nombre=nombre

    def cambiar_jefe(self, jefe):
        if self.__jefe=="":
            raise Exception ("Este departamento no tiene jefe, asignarlo con asignar_jefe")
        else:
            self.__jefe=jefe

    # def reclamos(self, reclamo):
    #     self.__reclamos_depto.append(reclamo)
