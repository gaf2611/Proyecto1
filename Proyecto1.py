import BaseDatos
import datetime
def inicio():
    while True:
        print("""
       |=================================|   
       | ¡BIENVENIDO! TALLER MECANICO GAF|
       |  Elija una opción:              |
       | 1. Opciones Administrativas.    |
       | 2. Consultas Técnicas.          |
       | 3. Salir.                       |
       |=================================|
        """)
        
        opcion = input("Selecciona una opción: ")
        if (opcion == "1"):
            menuAdmin()
        elif (opcion == "2"):
            menuConsulta()
        elif (opcion == "3"):
            break    
        else:
            print("Error: ¡Opción ingresada no existe! Ingrese una opción válida.")

    
def menuAdmin():
    while True:
        usuarioI = "TMG26"
        passwordI = "1234"
        print("Primero ingresa tus datos.")
        print ("Digite el usuario: ")
        usuario = input()
        print("Digite la contraseña: ")
        password = input()
        if (usuario == usuarioI) and (password == passwordI):
            BaseDatos.cargarDato('vehiculo')
            print("Has ingresado exitosamente al menú TMG ¡BIENVENIDO!") 

            print("""
            =============================
            |1. Gestión Tipo De Vehículo| 
            |2. Gestión de Repuestos    |
            |3. Gestión Mano De Obra    |
            |4. Gestión Mantenimiento   |
            |5. Gestión Reparaciones    |
            |6. Facturar                |
            |7. Salir                   |
            =============================
             """)
            opcion = input ("Digite una opción: ")
                
            #VEHICULO
            
            if  (opcion == "1"):
                print("""
                ========================================
                |GESTION DEL VEHICULO. ELIJA UNA OPCIÓN|
                |1. Agregar Vehículo.                  |
                |2. Modificar Vehículo.                |
                |3. Mostrar Vehículo.                  |
                |4. Eliminar Vehículo.                 |
                |5. Salir.                             |
                =========================================
                """)
                opcion = input ("Digite la opción que desea:")
                    
                if (opcion == "1"):
                    BaseDatos.agregarVehiculo()
                elif(opcion == "2"):
                    BaseDatos.modVehiculo()
                elif(opcion == "3"):
                    BaseDatos.mostrarVehiculo()
                elif(opcion == "4"):
                    BaseDatos.eliminarVehiculo()
                elif (opcion == "5"):
                    break
                else:
                    print("Error: Opción no válida. Vuelva a ingresar una opción.")
            #REPUESTO                     
            elif(opcion == "2"):
                print ("GESTION DE REPUESTOS. ELIJA UNA OPCIÓN")
                print("1. Agregar Repuesto. ")
                print("2. Modificar Repuesto. ")
                print("3. Mostrar Repuesto. ")
                print("4. Eliminar Repuesto. ")
                print("5. Salir. ")
                opcion = input ("Digite la opción que desea:")

                if (opcion == "1"):
                    BaseDatos.agregarRepuesto()
                elif (opcion == "2"):
                    BaseDatos.modRepuesto()
                elif (opcion == "3"):
                    BaseDatos.mostrarRepuesto()
                elif (opcion == "4"):
                    BaseDatos.eliminarRepuesto()
                elif (opcion == "5"):
                    break
                else:
                    print("Error: Opción no válida. Vuelva a ingresar una opción.")

            #MANO DE OBRA
            elif(opcion == "3"):
                print ("GESTION DE REPUESTOS. ELIJA UNA OPCIÓN")
                print("1. Agregar Mano De Obra. ")
                print("2. Modificar Mano De Obra. ")
                print("3. Mostrar Mano De Obra. ")
                print("4. Eliminar Mano De Obra. ")
                print("5. Salir. ")
                opcion = input ("Digite la opción que desea:")

                if (opcion == "1"):
                    BaseDatos.agregarManoObra()
                elif (opcion == "2"):
                    BaseDatos.modManoObra()
                elif (opcion == "3"):
                    BaseDatos.mostrarManoObra()
                elif (opcion == "4"):
                    BaseDatos.eliminarManoObra()
                elif (opcion == "5"):
                    break
                else:
                    print("Error: Opción no válida. Vuelva a ingresar una opción.")

            #MANTENIMIENTO  
            elif(opcion == "4"):
                print ("GESTION DE REPUESTOS. ELIJA UNA OPCIÓN")
                print("1. Agregar Mantenimiento. ")
                print("2. Modificar Mantenimiento. ")
                print("3. Mostrar Mantenimiento. ")
                print("4. Eliminar Mantenimiento. ")
                print("5. Salir. ")
                opcion = input ("Digite la opción que desea:")

                if (opcion == "1"):
                    BaseDatos.agregarMantenimiento()
                elif(opcion == "2"):
                    BaseDatos.modMantenimiento()
                elif(opcion == "3"):
                    BaseDatos.mostrarMantenimiento()
                elif (opcion == "4"):
                    BaseDatos.eliminarMantenimiento()

                
            elif(opcion == "5"):
                BaseDatos.reparaciones()
            elif(opcion == "6"):
                BaseDatos.facturar()
            elif(opcion == "7"):
                break
            else: 
                print ("¡Opción ingresada no valida! Ingrese un dato válido")        
        else:   
            print ("¡Usuario o contraseña no válido! Vuelva a ingresar los datos.")

def menuConsulta():
    while True:
        print("Bienvenido(a) al menú de consultas técnicas")
        print("Elija una de las opciones: ")
        print("1. Planes De Mantenimiento. ")
        print("2. Generar Reservación. ")
        print("3. Cancelar Reservación. ")
        print("4. consulta Reparación. ")
        print("5. consulta Facturación. ")
        print("6. Salir. ")
        opcion = input("Seleccione una opción:")
        if  (opcion == "1"):
            BaseDatos.planesM()
        elif(opcion == "2"):
            BaseDatos.genReservacion()
        elif(opcion == "3"):
            BaseDatos.cancelReservacion()
        elif(opcion == "4"):
            BaseDatos.consulReparacion()
        elif(opcion == "5"):
            BaseDatos.consulFacturacion()
        elif(opcion == "6"):
            break
        else:
            print("¡Opción NO es válida! ingrese de nuevo una opción.")
inicio()    
