entradas = [
    {
        "id" : "1",
        "nombre" : "Los Fortificados",
        "stock" : 10,
        "tipo" : "GV",
        "cliente" : ""
    },
    {
        "id" : "2",
        "nombre" : "Los Iluminados",
        "stock" : 15,
        "tipo" : "GV",
        "cliente" : ""
    }
    ]

def id_valida(id):
    id_numeros = "1234567890"
    for num in id:
        if num not in num or num <= 0:
            return False
        return True



def nombre_valido():
    for cliente in entradas:
        if cliente ["cliente"].lower() == cliente:
            print("Nombre ya ingresado.")
            return False
        if tipo != "G" and tipo != "V":
            print("El tipo de la pelicula solo puede ser G o V")
            return False
        if len(codigo) < 6:
            print("El codigo debe tener almenos 6 caracteres")
            return False
        elif len.upper(codigo).upper < 1:
            print("El codigo debe tener almenos una mayuscula.") 
            return False
        elif len(codigo) != "1234567890":
            print("El codigo debe tener almenos un numero")
            return False
        else:
            print("Entrada registrada correctamente. ")
            return True
 


def registrar_entrada():
    print("\n--- Registrar entrada ---")
    cliente = input("Ingrese el nombre del comprador: ")
    tipo = input("Ingrese el tipo de entrada (G/V): ").upper()
    codigo = input("Ingrese el codigo de confirmacion: ")
    















while True:
        print("--- TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE ---")
        print("1.- Comprar entrada a “los Fortificados”.")
        print("2.- Comprar entrada a “los Iluminados”.")
        print("3.- Stock de entradas para ambos conciertos.")
        print("4.- Salir.")
        opc = input("Ingrese el sistema a manejar: ")

        if opc == "1":
            nombre_valido()
            print("\n--- Registrar entrada ---")
            cliente = input("Ingrese el nombre del comprador: ")
            tipo = input("Ingrese el tipo de entrada (G/V): ").upper()
            codigo = input("Ingrese el codigo de confirmacion: ")
        

        elif opc == "4":
            print("Gracias por usar!")
            break
        else:
            print("Opcion no valida, intente otra vez.")
