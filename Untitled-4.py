c_dinero_ingresado = 0
c_total = 0
c_cambio = 0
def verificar_correo(correo):
    if 8 <= len(correo) <= 30:
        print("El correo es valido")
    else:
        print("Error: el correo tiene que tener entre 8 y 30 caracteres") 

print("Bienvenido a la màquina de arriendo de estacionamiento!")
correo = str(input("Ingresa tu correo: "))
ingreso_dinero = int(input("Ingresa un monto entre 1 y 10.000: "))
c_dinero_ingresado += ingreso_dinero

while True:
        try:
            if ingreso_dinero < 1:
                print("ingresa un monto valido")
                continue
            
            elif ingreso_dinero > 10000:
                print("Ingresa un monto valido")
                continue
            else:
                print("Vehículos:")
                print("1- Auto : 2000")
                print("2- Camioneta : 3000")
                print("3- Camión : 4000")
                print("4- Motocicleta : 890")
                print("5- Ingresar código de adm... ")
            seleccion = int(input("Seleccione una opción: "))

            if seleccion == 1 and c_dinero_ingresado >= 2000:
                print("Añadido : Auto ")
                c_total += 2000
                c_dinero_ingresado = c_dinero_ingresado - 2000
                c_dinero_ingresado = c_dinero_ingresado - c_cambio
            else:
                if seleccion == True:
                    continue
                print("Actualmente el dinero ingresado sería insuficiente para la opción 1.")
            
            if seleccion == 2 and c_dinero_ingresado >= 3000:
                print("Añadido : Camioneta ")
                c_total += 3000
                c_dinero_ingresado = c_dinero_ingresado - 3000
                c_dinero_ingresado = c_dinero_ingresado - c_cambio
            else:
                if seleccion == True:
                    continue
                print("Actualmente el dinero ingresado sería insuficiente para la opción 2.")

            
            if seleccion == 3 and c_dinero_ingresado >= 4000:
                print("Añadido : Camión ")
                c_total += 4000
                c_dinero_ingresado = c_dinero_ingresado - 4000
                c_dinero_ingresado = c_dinero_ingresado - c_cambio
            else:
                if seleccion == True:
                    continue
                print("Actualmente el dinero ingresado sería insuficiente para la opción 3.")
            

            
            if seleccion == 4 and c_dinero_ingresado >= 890:
                print("Añadido : Motocicleta ")
                c_total += 890
                c_dinero_ingresado = c_dinero_ingresado - 890
                c_dinero_ingresado = c_dinero_ingresado - c_cambio

            else:
                if seleccion == True:
                    continue
                print("Actualmente el dinero ingresado sería insuficiente para la opción 4.")
        except ValueError:
            print("Valor ingresado invalido ingresa otro")
        print(f"Total: " , c_total)












