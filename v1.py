class cajeroAutomatico:
    def __init__(self):
        with open("datos.txt", "r") as archivo:
            lineas = archivo.readlines()
        # acceso
        self.usuario = lineas[0].strip()
        self.contrasena = lineas[1].strip()

        # datos de cuenta
        self.saldo = int(lineas[2].strip())
        self.limite_extraccion = int(lineas[3].strip())

        # registro de operaciones
        self.historial = []
        self.contador_operaciones = 0

#inicio sesion
def iniciar_sesion(self):
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario == self.usuario and contrasena == self.contrasena:
        print("\nAcceso concedido.")
        return True
    else:
        print("\nUsuario o contraseña incorrectos.")
        return False
    
#Consultar saldo
def consultar_saldo(self):
    print(f"\nSaldo disponible: ${self.saldo:.2f}")
    self.historial.append("Consulta de saldo")
    self.contador_operaciones += 1

#deposito
def depositar(self):
    try:
        monto = float(input("Ingrese el monto a depositar: $"))

        if monto <= 0:
            print("Error: El monto debe ser mayor que cero.")
        else:
            self.saldo += monto
            self.historial.append(f"Se han agregado a su cuenta: ${monto:.2f}")
            self.contador_operaciones += 1
            print("Deposito exitoso.")

    except ValueError:
        print("Error: Ingrese numero valido.")

#extraccion
def extraer(self):
    try:
        monto = float(input("Ingrese el monto que desea extraer: $"))

        if monto <= 0:
            print("Error: El monto debe ser mayor que cero.")
        elif monto > self.saldo:
            print("Error: Fondos insuficientes.")
        elif monto > self.limite_extraccion:
            print(f"Error: El monto excede el límite de extracción de ${self.limite_extraccion:.2f}.")
        else:
            self.saldo -= monto
            self.historial.append(f"Se han retirado de su cuenta: ${monto:.2f}")
            self.contador_operaciones += 1
            print("Extracción exitosa.")

    except ValueError:
        print("Error: Ingrese numero valido.")

#transferencia

def transferir(self):
    try:
        monto = float(input("Ingrese el monto que desea transferir: $"))
        cbu = int(input("Ingrese el CBU del destinatario: "))
        if monto <= 0:
            print("Error: El monto debe ser mayor que cero.")
        elif monto > self.saldo:
            print("Error: Fondos insuficientes.")
        else:
            self.saldo -= monto
            self.historial.append(f"Se han transferido de su cuenta: ${monto:.2f}")
            self.contador_operaciones += 1
            print("Transferencia exitosa.")

    except ValueError:
        print("Error: Ingrese numero valido.")

def guardar_datos(self):
    with open("datos.txt", "w") as archivo:
        archivo.write(f"{self.usuario}\n")
        archivo.write(f"{self.contrasena}\n")
        archivo.write(f"{self.saldo}\n")
        archivo.write(f"{self.limite_extraccion}\n")        

iniciar = input("¿Desea iniciar sesión? (s/n): ")
if iniciar == 's':
    cajero = cajeroAutomatico()
    sesion = iniciar_sesion(cajero)
    if sesion:
        while True:
            print("\nSeleccione una opción:")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Extraer dinero")
            print("4. Transferir dinero")
            print("5. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                consultar_saldo(cajero)
            elif opcion == '2':
                depositar(cajero)
            elif opcion == '3':
                extraer(cajero)
            elif opcion == '4':
                transferir(cajero)
            elif opcion == '5':
                print("Gracias por usar el cajero automático. ¡Hasta luego!")
                guardar_datos(cajero)
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")
else:
    print("Sesión no iniciada. ¡Hasta luego!")
