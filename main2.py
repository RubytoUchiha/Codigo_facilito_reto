### Reto 2 

cantidad_usuarios = int(input("Ingrese la cantidad de usuarios que desea registrar: "))

while cantidad_usuarios <= 0:
    print("La cantidad de usuarios debe ser mayor que 0.")
    cantidad_usuarios = int(input("Ingrese la cantidad de usuarios que desea registrar: "))

usuarios = []

for i in range(cantidad_usuarios):
    print(f"\nIngrese los datos del usuario {i+1}:")
    
    nombre = input("Ingrese el nombre del usuario: ")
    while not (5 <= len(nombre) <= 50):
        print("El nombre debe tener entre 5 y 50 caracteres.")
        nombre = input("Ingrese el nombre del usuario: ")

    apellidos = input("Ingrese los apellidos del usuario: ")
    while not (5 <= len(apellidos) <= 50):
        print("Los apellidos deben tener entre 5 y 50 caracteres.")
        apellidos = input("Ingrese los apellidos del usuario: ")

    telefono = input("Ingrese el número de teléfono del usuario: ")
    while not (len(telefono) == 10 and telefono.isdigit()):
        print("El número de teléfono debe tener exactamente 10 dígitos.")
        telefono = input("Ingrese el número de teléfono del usuario: ")

    correo = input("Ingrese el correo electrónico del usuario: ")
    while not (5 <= len(correo) <= 50 and '@' in correo and '.' in correo):
        print("El correo electrónico debe tener entre 5 y 50 caracteres y ser válido.")
        correo = input("Ingrese el correo electrónico del usuario: ")

    usuario_str = f"Nombre: {nombre}, Apellidos: {apellidos}, Teléfono: {telefono}, Correo electrónico: {correo}"
    usuarios.append(usuario_str)

print("\nUsuarios registrados:")

for i, usuario in enumerate(usuarios, start=1):
    print(f"\nUsuario {i}: {usuario}")
