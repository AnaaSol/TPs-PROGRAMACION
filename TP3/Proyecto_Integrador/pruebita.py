# from modules.config import app, db
# from modules.gestores import Gestor_de_base_de_datos

# Gestor=Gestor_de_base_de_datos()
# with app.app_context():
#     db.create_all()
#     Gestor.modificar_dato("estado", "pendiente", "reclamo", 2) #probé en vez d ependiente con un número
#     #controlar con isinstance por fuera del método antes de enviar el datos al gestor
#     #capturar excepciones por fuera de los métodos

listita=""

listita2=listita+" "+"blast"+" "+"esto debería creo"
listita3=listita+"blast"+"esto debería creo"

print("listita=", listita)
print("listita2=", listita2)
print("listita2 divida=", listita2.split(" "))

a=["pero", "la", "concha", "de", "la", "lora"]
print(a)
print(a[0])
print(a[-1])

funny=["it should remain this way"]
empty=[]

for a in empty:
    print("entró")
    data="blabla"
    funny.append(data)

print(funny)
print(len(empty))
print(empty[-1])