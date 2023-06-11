from modulos.classes import *

FIUNER=Facultad("Matemática")

#en la composición el objeto miembro no existe por fuera del contenedor
#Depto_informática=FIUNER.Crear_departamento("Informática")

FIUNER.Crear_departamento("Informática")

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

FIUNER.Agregar_profesor_a_depto("Informática", Bruno)
print(Bruno.depto)
#FIUNER.Asignar_director_a_depto("Informática", Javier) #funciona la excepción
FIUNER.Agregar_profesor_a_depto("Informática", Javier)
print(Javier.depto)
FIUNER.Asignar_director_a_depto("Informática", Javier)
print(Javier.director)

