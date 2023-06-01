from modulos.classes import *

FIUNER=Facultad("Matemática")

#cómo hago para que los departamentos sólo puedan ser creados desde facultad?
#Depto_informática=Departamento()

Depto_informática=FIUNER.Crear_departamento("Informática")

Ana=Estudiante()
Ana.set_nombre("Ana")
Ana.set_apellido("Murzi")
Ana.set_edad(18)
Ana.set_DNI("45043509")

Paula=Estudiante()
Paula.set_nombre("Paula")
Paula.set_apellido("Demartini")
Paula.set_edad(18)
Paula.set_DNI("45737902")

Javier=Profesor()
Javier.set_nombre("Javier")
Javier.set_apellido("Diaz Zamboni")

Bruno=Profesor()
Bruno.set_nombre("Bruno")
Bruno.set_apellido("Breggia")
Bruno.set_edad(22)
Bruno.set_DNI("40998123")

Avanzada=Curso("Avanzada")
Avanzada.Asignar_profesor(Bruno)
Avanzada.Asignar_profesor(Javier)
Avanzada.Asignar_jdc(Javier)

FIUNER.Agregar_estudiante(Paula)
FIUNER.Agregar_estudiante(Ana)

Ana.Matricularse(Avanzada)
Paula.Matricularse(Avanzada)
Avanzada.Listar()

print(Avanzada.cupo)

Ana.Darse_de_baja(Avanzada)
Avanzada.Listar()
Avanzada.Asignar_jdc(Javier)
print(Avanzada.cátedra)
print(Bruno.cursos)
Bruno.Renunciar(Avanzada)
print(Bruno.cursos)
print(Avanzada.cátedra)
print(Bruno.depto)
#FIUNER.departamentos[0].Agregar_profesor(Bruno)
#Depto_informática.Agregar_profesor(Bruno) #en la composición el objeto miembro no existe por fuera del contenedor
FIUNER.departamentos[1].Agregar_profesor(Bruno)
print(Bruno.depto)
#FIUNER.departamentos[1].Asignar_director(Javier) #funciona la excepción
FIUNER.departamentos[1].Agregar_profesor(Javier)
FIUNER.departamentos[1].Asignar_director(Javier)
print(FIUNER.departamentos[1].director)

#cuidado con la información cíclica




