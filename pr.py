import datetime

def inicio():
    while True:
        print("""
            ====================================   
            ⚛ ¡BIENVENIDO! TALLER MECANICO GAF⚛
            ⚛  Elija una opción:              ⚛
            ⚛ 1. Opciones Administrativas.    ⚛
            ⚛ 2. Consultas Técnicas.          ⚛
            ⚛ 3. Salir.                       ⚛
            ====================================
        """)
        
        opcion = input("Selecciona una opción: ")
        if (opcion == "1"):
            datosAdministrativos()
        elif (opcion == "2"):
            menuConsulta()
        elif (opcion == "3"):
            break    
        else:
            print("Error: ¡Opción ingresada no existe! Ingrese una opción válida.")

#Validar Datos De Administrador
def datosAdministrativos():
    print("""
        ============================================================
        Para acceder a la opcion administrativa debes iniciar sesión
        ============================================================
    """)

    usuario = input("Ingrese el  usuario: ")
    print("\n")
    if (usuario != ""):
        contraseña = input(f"Ingrese la contraseña valida para el usuario {usuario}: ")
        print("\n")
    
        if (contraseña != ""):
            buscarDato = f"{usuario},{contraseña}"
        
            archivo = open("datos.txt", encoding = "utf-8", mode = "r")
            datos = archivo.readline().strip()
            archivo.close()

            encontrado = False
            for dato in  datos:
                if  buscarDato ==  datos:
                    encontrado = True
                    
            if encontrado == True:
                print("==========================================")
                print("¡Bienvenido!, MENU ADMINISTRATIVO TMG S.A")
                print("==========================================")
                
                return menuAdmin()
            
            else:
                print("#######################################################")
                print("\n")
                print("Error: Datos ingresados no son correctos. Intentalo de nuevo.")
                print("\n")
                print("#######################################################")
                return datosAdministrativos()
            
        else:
            print("=======================================")
            print("\n")
            print("Error: La contraseña debe ser diferente a vacío.")
            return datosAdministrativos()            
    else:
        print("=======================================")
        print("\n")
        print("Error: El usuario debe ser diferente a vacío")
        return datosAdministrativos()
    


def menuAdmin():

    while True:
        print("Seleccione una de las opciones:")
        print("1. Gestión Tipo De Vehículo ")
        print("2. Gestión de Repuestos ")
        print("3. Gestión Mano De Obra ")
        print("4. Gestión Mantenimiento ")
        print("5. Gestión Reparaciones ")
        print("6. Facturar ")
        print("7. Salir ")
        opcion = input ("Digite una opción: ")
        opcion = opcion.upper()
        print("\n")
    
        if (opcion != ""):
                
            if opcion == "1":
#VEHICULO
                if  (opcion == "1"):
                    print ("GESTION DEL VEHICULO. ELIJA UNA OPCIÓN")
                    print("1. Agregar Vehículo. ")
                    print("2. Modificar Vehículo. ")
                    print("3. Mostrar Vehículo. ")
                    print("4. Eliminar Vehículo. ")
                    print("5. Salir. ")
                        
                    print("\n")
                    opcion = input ("Digite la opción que desea:")
                    if (opcion == "1"):
                        agregarVehiculo()
                    elif (opcion == "2"):
                        modVehiculo()
                    elif (opcion == "3"):
                        mostrarVehiculo()
                    elif (opcion == "4"):
                        eliminarVehiculo()
                    elif (opcion == "5"):
                        break
                    else:
                        print("Error: Opción no válida. Vuelva a ingresar una opción.")
                    
                elif opcion == "2":
                    print ("GESTION DE REPUESTOS. ELIJA UNA OPCIÓN")
                    print("1. Agregar Repuesto. ")
                    print("2. Modificar Repuesto. ")
                    print("3. Mostrar Repuesto. ")
                    print("4. Eliminar Repuesto. ")
                    print("5. Salir. ")
                    opcion = input ("Digite la opción que desea:")
                    
                elif opcion == "3":
                    return borrarProducto()

                elif opcion == "4":
                    return agregarInventario()
                
                elif opcion == "5":
                    return ReportesInventario()
                
                elif opcion == "6":
                    return menu()
                
                elif opcion == "7":
                    return salir()
                    
                else:
                    print("=======================================")
                    print("\n")
                    print("Error: Opción no reconocida")
                    return menuAdmin()
        else:
            print("=======================================")
            print("\n")
            print("Error: El parámetro de entrada no debe ser vacio")
            return menuAdmin()    

#FUNCION AGREGAR PARA TODAS LAS GESTIONES#

def agregarVehiculo():

    print("=======================================")
    print("            Agregar Vehiculo          ")
    print("=======================================")

    codigo = codigo_Aux()
    print("\n")
    tipoVehiculo = input("Ingrese el tipo de vehículo que desea ingresar: ")
    tipoVehiculo = tipoVehiculo.title()
    print("\n")
    pasajeros= input("Ingrese la cantidad de pasajeros que contiene el vehículo: ")

    print("\n")
    ejes = input("Ingrese la cantidad de ejes del vehículo: ")
    

    if (tipoVehiculo != "") and (pasajeros != "") and (ejes != ""):

        try:
            pasajeros = int(pasajeros)
            ejes = int(ejes)
        except:
            print("Error: Se debe colocar un valor númerico para los ejes o pasajeros")
            return agregarVehiculo()
        else:
        
            infoVehiculo = f"{codigo};{tipoVehiculo};{pasajeros};{ejes}"

            archivo = open("Vehiculo.txt", encoding = "utf-8", mode = "r")
            lineas = archivo.readlines()
            archivo.close()

            if lineas != "":
            
                encontrado = False

                for linea in lineas:
                
                    cont = linea.strip().split(";")
                    encontrar = cont[1]

                    if tipoVehiculo == encontrar:
                        encontrado = True
                        print(f" se encontró un tipo de vehiculo con el nombre {tipoVehiculo},")
                        print("Porfavor ingresa otro tipo de vehículo o modificalo.")
                        return menuAdmin()

            if encontrado == False:
                archivo = open("Vehiculo.txt", encoding = "utf-8", mode = "a")
                archivo.write(f"{infoVehiculo}")
                archivo.close()
            print("¡Vehiculo agregado con exito!")
            return menuAdmin()
        
    else:
        print("Error: Los parámetros de entrada no deben ser vacios")
        return agregarVehiculo()
    ##########################################################################
    def agregarRepuesto():

        print("=======================================")
        print("            Agregar Repuesto          ")
        print("=======================================")

        codigo = codigo_Aux()
       
        nombreR = input("Ingrese el nombre del repuesto que desea ingresar: ")
        nombreR = nombreR.title()
        
        costoCompra= input("Ingrese el costo del repuesto: ")

        print("\n")
        precioVenta = input("Ingrese el precio de venta para el repuesto: ")
        

        if (nombreR != "") and (costoCompra != "") and (precioVenta != ""):

            try:
                costoCompra = int(costoCompra)
                precioVenta = int(precioVenta)
            except:
                print("Error: Se debe colocar un valor númerico para el costo del repuesto o el precio de venta del mismo.")
                return agregarRepuesto()
            else:
            
                infoRepuesto = f"{codigo};{tipoVehiculo};{pasajeros};{ejes}"

                archivo = open("repuestos.txt", encoding = "utf-8", mode = "r")
                lineas = archivo.readlines()
                archivo.close()

                if lineas != "":
                
                    encontrado = False

                    for linea in lineas:
                    
                        cont = linea.strip().split(";")
                        encontrar = cont[1]

                        if nombreR == encontrar:
                            encontrado = True
                            print(f" se encontró un tipo de repuesto con el nombre {nombreR},")
                            print("Porfavor ingresa otro tipo de repuesto o modificalo.")
                            return menuAdmin()

                if encontrado == False:
                    archivo = open("repuestos.txt", encoding = "utf-8", mode = "a")
                    archivo.write(f"{nombreR}")
                    archivo.close()
                print("¡Repuesto fue agregado con exito!")
                return menuAdmin()
            
        else:
            print("Error: Los parámetros de entrada no deben ser vacios")
            return agregarRepuesto() 
############################################################################################
def agregarManoObra():
        print("=======================================")
        print("         Agregar Mano De Obra          ")
        print("=======================================")

        codigo = codigo_Aux()
       
        nombreR = input("Ingrese el nombre del repuesto que desea ingresar: ")
        nombreR = nombreR.title()
        
        costoCompra= input("Ingrese el costo del repuesto: ")

        print("\n")
        precioVenta = input("Ingrese el precio de venta para el repuesto: ")
        

        if (nombreR != "") and (costoCompra != "") and (precioVenta != ""):

            try:
                costoCompra = int(costoCompra)
                precioVenta = int(precioVenta)
            except:
                print("Error: Se debe colocar un valor númerico para el costo del repuesto o el precio de venta del mismo.")
                return agregarRepuesto()
            else:
            
                infoRepuesto = f"{codigo};{tipoVehiculo};{pasajeros};{ejes}"

                archivo = open("repuestos.txt", encoding = "utf-8", mode = "r")
                lineas = archivo.readlines()
                archivo.close()

                if lineas != "":
                
                    encontrado = False

                    for linea in lineas:
                    
                        cont = linea.strip().split(";")
                        encontrar = cont[1]

                        if nombreR == encontrar:
                            encontrado = True
                            print(f" se encontró un tipo de repuesto con el nombre {nombreR},")
                            print("Porfavor ingresa otro tipo de repuesto o modificalo.")
                            return menuAdmin()

                if encontrado == False:
                    archivo = open("repuestos.txt", encoding = "utf-8", mode = "a")
                    archivo.write(f"{nombreR}")
                    archivo.close()
                print("¡Repuesto fue agregado con exito!")
                return menuAdmin()
            
        else:
            print("Error: Los parámetros de entrada no deben ser vacios")
            return agregarRepuesto() 


"--------------------------------------------------------------------------------"

"""
Nombre: modificarProducto
Entrada: código
Salida: La posibilidad de poder modificar el nombre del producto, categorías
        y precio unitario.
Restricciones:
             ¬ El código debe ser existente y valido (númerico)
             
"""

def modificarProducto():
    
    print("\n")
    print("=======================================")
    print("\n")
    print("          Modificar Producto           ")
    print("\n")
    print("=======================================")
    print("\n")

    mostrar = mostrar_Auxi()
    print("\n") 
    codigo = input("Digite el código de la línea a modificar: ")
    print("\n")
    
    if (codigo != ""):
        try:
            codigo = int(codigo)
        except:
            print("Error: El código ingresedo debe ser númerico")
            return modificarProducto()
        else:
            if codigo < 0:
                print("=======================================")
                print("\n")
                print("Error: El codigo no puede ser negativo.")
                return modificarProducto()
            
            archivo = open("Inventario.txt", encoding="utf-8", mode="r")
            lineas = archivo.readlines()
            archivo.close()

            nuevasLineas = []
            modificarLinea = False

            for linea in lineas:
                codigoLinea = int(linea.split(';')[0])  
                
                if codigoLinea == codigo:
                    modificarLinea = True

                    print("=======================================")
                    print("\n")
                    print("La linea a modificar es: ")
                    print("\n")
                    print(linea)
                    print("\n")
                    print("=======================================")
                    print("\n")
    
                    producto = input("Ingrese el nombre del producto que\ndeseas agregar a tu inventario: ")
                    producto = producto.title()
                    print("\n")
                    categoria = input("Ingrese la categoría del producto que\ndeseas agregar a tu inventario: ")
                    categoria = categoria.capitalize()
                    print("\n")
                    precioUnitario = input("Ingrese el valor unitario del producto que\ndeseas agregar a tu inventario: ")
                    cantidad = (linea.split(';')[4])  
                    print("\n")
                    
                    if (producto != "") and (categoria != "") and (precioUnitario != ""):

                        try:
                            precioUnitario = int(precioUnitario)
                        except:
                            print("=======================================")
                            print("\n")
                            print("Error: debes ingresar un valor númerico para el precio")
                            return modificarProducto()
                        else:
                            
                            archivo = open("Inventario.txt", encoding = "utf-8", mode = "r")
                            lineas = archivo.readlines()
                            archivo.close()

                            if lineas != "":
            
                                encontrado = False

                                for linea in lineas:
                
                                    contenido = linea.strip().split(";")
                                    productoBuscar = contenido[1]
                                    
                                    if producto == productoBuscar or codigoLinea != codigo:
                                        encontrado = True
                                        print("=======================================")
                                        print("\n")
                                        print(f"Se ha encontrado un producto registrado con el nombre {producto}")
                                        print("El registro es: ")
                                        print("\n")
                                        print(linea)
                                        print("\n")
                                        print("Modifica este registro o ingresa otro producto")
                                        print("\n")
                                        return inventario()

                                if encontrado == False:
                            
                                    nuevaLinea = f"{codigo};{producto};{categoria};{precioUnitario};{cantidad}"
                                    nuevasLineas += [nuevaLinea]
                    else:
                        print("=======================================")
                        print("\n")
                        print("Error: Los parámetros de entrada no deben ser vacios")
                        return modificarProducto()
                            
                else:
                    nuevasLineas += [linea]

            if modificarLinea == True:
                
                archivo = open("Inventario.txt",encoding="utf-8", mode = 'w')
                archivo.writelines(nuevasLineas)
                archivo.close()
                
                print("=======================================")
                print("\n")
                print(f"La línea con código {codigo} ha sido modificada con éxito.")
                return inventario()
            
            else:
                print("=======================================")
                print("\n")
                print(f"No se encontró ninguna línea con código {codigo} en el inventario.")
                return modificarProducto()
    else:
        print("=======================================")
        print("\n")  
        print("Error: El código no debe ser vacio")
        return modificarProducto()
    
"--------------------------------------------------------------------------------"

"""
Nombre: borrarProducto
Entrada: código
Salida: La posibilidad de poder borrar la linea con el código 
Restricciones:
             ¬ El código debe ser existente y valido (númerico positivo)
             
"""

def borrarProducto():
    
    print("\n")
    print("=======================================")
    print("\n")
    print("          Borrar Producto              ")
    print("\n")
    print("=======================================")
    print("\n")

    mostrar = mostrar_Auxi()
    print("\n")
    codigo = input("Digite el código de la línea a borrar: ")
    print("\n")

    if (codigo != ""):
        try:
            codigo = int(codigo)
        except:
            print("=======================================")
            print("\n")
            print("Error: El código ingresedo debe ser númerico")
            return borrarProducto()
        else:  
            if codigo < 0:
                print("=======================================")
                print("\n")
                print("Error: El codigo no puede ser negativo.")
                return borrarProducto()
            
            archivoI = open("Inventario.txt", encoding="utf-8", mode="r")
            lineasI = archivoI.readlines()
            archivoI.close()

            archivoFD = open("FacturasDetalle.txt", encoding="utf-8", mode="r")
            lineasFD = archivoFD.readlines()
            archivoFD.close()
            
            nuevasLineas = []
            borrarLinea = False

            facturado = False
            for lineaI in lineasI:
                contenidoI = lineaI.split(';')
                codigoLineaI = int(contenidoI[0])
                
                if codigoLineaI == codigo:

                    productoI = contenidoI[1]

                    for lineaFD in lineasFD:
                        contenidoFD = lineaFD.split(',')
                        productoFD = contenidoFD[2]

                        if productoI == productoFD:
                            facturado = True

                        if facturado == True:
                            print(f"\nEl código {codigo} le pertenece al producto {productoFD} el cual está facturado, por normativa,")
                            print("no es posible efectuar la eliminación de este producto en el inventario. Por favor, ingrese otro")
                            print("código a borrar.")
                            return borrarProducto()

                    print("=======================================")
                    print("\n")
                    print("La linea a borrar es: ")
                    print("\n")
                    print(lineaI)
                    print("\n")
                    print("=======================================")
                    print("\n")

                    confirmacion = input("¿Estás seguro que deseas borrar esta línea? (Y/N): ")
                    confirmacion = confirmacion.capitalize()
                    print("\n")
                    
                    if confirmacion == "Y":
                        print("=======================================")
                        print("\n")
                        print(f"La línea con código {codigo} ha sido borrada con éxito.")
                        print("\n")
                        print("=======================================")
                        print("\n")
                        borrarLinea = True
                        
                    elif confirmacion == "N":
                        print("=======================================")
                        print("\n")
                        print(f"La línea con código {codigo} no ha sido borrada.")
                        print("\n")
                        print("=======================================")
                        print("\n")
                        return inventario()
                
                    else:
                        print("=======================================")
                        print("\n")
                        print("Error: opcion no reconocida")
                        return borrarProducto()
                                          
                else:
                    nuevasLineas += [lineaI]

            if borrarLinea == True:
                
                archivo = open("Inventario.txt",encoding="utf-8", mode = 'w')
                archivo.writelines(nuevasLineas)
                archivo.close()
                return inventario()
            
            else:
                print("=======================================")
                print("\n")
                print(f"No se encontró ninguna línea con código {codigo} en el inventario.")
                return borrarProducto()
    else:
        print("=======================================")
        print("\n")        
        print("Error: El código no debe ser vacio")
        return borrarProducto()
    
"--------------------------------------------------------------------------------"

"""
Nombre: agregarInventario
Entrada: código
Salida: La posibilidad de poder agregar inventario a la linea con el código 
Restricciones:
             ¬ El código debe ser existente y valido (númerico positivo)
             
"""

def agregarInventario():

    print("\n")
    print("=======================================")
    print("\n")
    print("          Agregar Inventario           ")
    print("\n")
    print("=======================================")
    print("\n")

    mostrar = mostrar_Auxi()
    print("\n")
    codigo = input("Digite el código del inventario a agregar: ")
    print("\n")

    if (codigo != ""):
        try:
            codigo = int(codigo)
        except:
            print("=======================================")
            print("\n")
            print("Error: El código ingresedo debe ser númerico")
            return agregarInventario()
        else:
            if codigo < 0:
                print("=======================================")
                print("\n")
                print("Error: El codigo no puede ser negativo.")
                return agregarInventario()
            
            archivo = open("Inventario.txt", encoding="utf-8", mode="r")
            lineas = archivo.readlines()
            archivo.close()
            
            nuevasLineas = []
            Inventario = False

            for linea in lineas:
                codigoLinea = int(linea.split(';')[0])  
                
                if codigoLinea == codigo:
                    Inventario = True

                    print("=======================================")
                    print("\n")
                    print("La linea del inventario a agregar es: ")
                    print("\n")
                    print(linea)
                    print("=======================================")
                    print("\n")
                    
                    producto = (linea.split(';')[1]) 
                    categoria = (linea.split(';')[2]) 
                    precioUnitario = (linea.split(';')[3])
                    cantidadRegistrada = int(linea.split(';')[4])
                    cantidad = input("Ingrese la cantidad del producto: ")
                    print("\n")

                    if (cantidad != ""):
                        try:
                            cantidad = int(cantidad)
                        except:
                            print("=======================================")
                            print("\n")
                            print("Error: La cantidad ingreseda debe ser númerica")
                            return agregarInventario()
                        else:
                            if cantidad < 0:
                                print("=======================================")
                                print("\n")
                                print("Error: La cantidad de inventario no puede ser negativa.")
                                return agregarInventario()

                            nuevaCantidad = cantidad + cantidadRegistrada
                            nuevaLinea = f"{codigo};{producto};{categoria};{precioUnitario};{nuevaCantidad}\n"
                            nuevasLineas += [nuevaLinea]
                    else:
                        print("=======================================")
                        print("\n")
                        print("Error: El parámetro de entrada debe ser númerico positivo")
                        return agregarInventario()
                        
                else:
                    nuevasLineas += [linea]

            if Inventario == True:
                
                archivo = open("Inventario.txt",encoding="utf-8", mode = 'w')
                archivo.writelines(nuevasLineas)
                archivo.close()

                print("=======================================")
                print("\n")
                print(f"El inventario con código {codigo} ha sido agregado con éxito.")
                return inventario()
            
            else:
                print("=======================================")
                print("\n")
                print(f"No se encontró ningun inventario con código {codigo} en el inventario.")
                return agregarInventario()
    else:
        print("=======================================")
        print("\n")        
        print("Error: El código no debe ser vacio")
        return agregarInventario()
    
"--------------------------------------------------------------------------------"

"""
Nombre: ReportesInventario
Entrada: opcion
Salida: Direccionar al usuario a la opción seleccionada
Restricciones:
             ¬ La opción no debe ser vacia
             ¬ La opción debe estar en el parámetro mostrado
"""

def ReportesInventario():
    
    print("\n")
    print("=======================================")
    print("\n")
    print("       Menú Reportes de Inventario     ")
    print("\n")
    print("=======================================")
    print("\n")
    print("Opciones:")
    print("       RP: Reportes de productos")
    print("\n")
    print("       RC: Reportes por categoría")
    print("\n")
    print("       RE: Reportes por Existencia")
    print("\n")
    print("       M: Volver al menú principal")
    print("\n")
    print("       I: Volver al menú inventario")
    print("\n")
    print("       S: Salir")
    print("\n")

    opcion = input("Ingrese la opción deseada: ")
    opcion = opcion.upper()
    print("\n")

    if (opcion != ""):
                
        if opcion == "RP":
            return reportesProductos()
            
        elif opcion == "RC":
            return reportesCategoria()
            
        elif opcion == "RE":
            return reportesExistencia()

        elif opcion == "M":
            return menu()
        
        elif opcion == "I":
            return inventario()
        
        elif opcion == "S":
            return salir()
            
        else:
            print("=======================================")
            print("\n")
            print("Error: Opción no reconocida")
            return ReportesInventario()
    else:
        print("=======================================")
        print("\n")
        print("Error: El parámetro de entrada no debe ser vacio")
        return ReportesInventario()     

"--------------------------------------------------------------------------------"

"""
Nombre: reportesProductos
Entrada: --
Salida: Devuelve el contenido del inventario, en caso de no haber registros
        se devuelve el mensaje correspondiente.
Restricciones: --
"""
def reportesProductos():

    print("\n")
    print("=======================================")
    print("\n")
    print("         Reporte de Productos          ")
    print("\n")
    print("=======================================")
    print("\n")
    
    
    archivo = open ("Inventario.txt", encoding = "utf-8", mode = "r")
    contenido = archivo.readlines()
    archivo.close()
    
    fechaActual = datetime.date.today().strftime("%d/%m/%Y")
    horaActual = datetime.datetime.now().strftime("%I:%M:%p")
    nuevasLineas = []

    if largoTexto_Aux(contenido) != 0:
        
        for linea in contenido:
            
            codigo = (linea.split(';')[0]) 
            producto = (linea.split(';')[1])  
            precioUnitario = (linea.split(';')[3]) 
            cantidad = (linea.split(';')[4]) 

            nuevaLinea = f"{codigo}\t\t{producto}\t\t\t{precioUnitario}₡\t\t\t{cantidad}\n"
            nuevasLineas += [nuevaLinea]
           
        print(".......................................")
        print("           Inicio Reporte              ")
        print(".......................................")
        print("\n")
        print("Código\t\tProducto\t\tPrecio Unitario\t\tCantidad")
        print("\n")
        for linea in nuevasLineas:
            print(linea)
        print(".......................................")
        print("              Fin Reporte              ")
        print(".......................................")
        print("\n")
        print("=======================================")
    
        guardar = input("\n¿Desea guardar el reporte de productos en un archivo externo?[Y/N]: ")
        guardar = guardar.capitalize()
        print("\n")

        while guardar != "Y" and guardar != "N":
                    
            print("=======================================")
            print("\n")
            print("Error: Opción inválida. Intenta de nuevo.")
            print("\n")
            print("=======================================")
            print("\n")

            guardar = input("¿Desea guardar el reporte de productos en un archivo externo?[Y/N]: ")
            guardar = guardar.capitalize()    
            print("\n")
            
        if guardar == "Y":
            
            archivoExterno = input("Ingrese el nombre del archivo: ")
            archivo = open(archivoExterno + ".txt", encoding="utf-8", mode="a")
            archivo.write("..........................................................................\n")
            archivo.write("                       REPORTE DE PRODUCTOS                               \n")
            archivo.write(f"Reporte generado el {fechaActual}\n\t\t\t\t\t{horaActual}\n")
            archivo.write("Código\tProducto\tPrecio Unitario\t\tCantidad\n")
            for linea in nuevasLineas:
                archivo.write(linea)
            archivo.write("\n..........................................................................\n\n")
            archivo.close()
            print("\n")
            print("El reporte de productos ha sido guardado exitosamente.")
            return ReportesInventario()
        else:
            print("\n")
            print("Reporte de productos finalizado")
            return ReportesInventario()
    
    else:
        print("Aún no haz realizado ningún registro de inventario.")
        print("Te vamos a redireccionar al aparatado de 'inventario'")
        print("para que realices los registros correspodientes.")
        return inventario()

"--------------------------------------------------------------------------------"

"""
Nombre: reportesCategoria
Entrada: categoría
Salida: Devuelve el contenido del inventario que tengan coincidencias con la
        categoría ingresada.
Restricciones:
             ¬ El parámetro de entrada no debe ser vacio
"""

def reportesCategoria():
    
    print("\n")
    print("=======================================")
    print("\n")
    print("        Reporte por Categoría          ")
    print("\n")
    print("=======================================")
    print("\n")

    fechaActual = datetime.date.today().strftime("%d/%m/%Y")
    horaActual = datetime.datetime.now().strftime("%I:%M:%p")
    nuevasLineas = []

    categoriaBuscar = input("Ingrese la categoría a buscar: ")
    print("\n")
    categoriaBuscar = categoriaBuscar.capitalize()

    archivo = open ("Inventario.txt", encoding = "utf-8", mode = "r")
    contenido = archivo.readlines()
    archivo.close()
    
    if categoriaBuscar != "":
        
        largoCategoriaBuscar = largoTexto_Aux(categoriaBuscar)
        
        if largoTexto_Aux(contenido) != 0:
            encontrado = False
            for linea in contenido:
                
                categoria = (linea.split(';')[2]).strip()
                categoriaCorte = categoria[0:largoCategoriaBuscar]

                if categoriaBuscar == categoriaCorte:
                    encontrado = True
                    contenido = linea.split(';')
                    codigo = contenido[0] 
                    producto = contenido[1]
                    precioUnitario = contenido[3]
                    cantidad = contenido[4]
                    categoriaEncontrada = contenido[2]
                    
                    nuevaLinea = f"{codigo}\t\t{producto}\t\t\t{precioUnitario}₡\t\t\t{cantidad}\n"
                    nuevasLineas += [nuevaLinea]
                    
            if encontrado == False:
                print(f"No se ha encontrado registro con la categoría {categoriaBuscar}")
                print("Verifique que la categoria registrada es correcta.")
                return reportesCategoria()
        
            print(".......................................")
            print("           Inicio Reporte              ")
            print(".......................................")
            print("\n")
            print("Código\t\tProducto\t\tPrecio Unitario\t\tCantidad")
            print("\n")
            for linea in nuevasLineas:
                    print(linea)
            print("\n")
            print(".......................................")
            print("              Fin Reporte              ")
            print(".......................................")
            print("\n")
            print("=======================================")

            guardar = input("¿Desea guardar el reporte de productos en un archivo externo?[Y/N]: ")
            guardar = guardar.capitalize()    
            print("\n")
            
            while guardar != "Y" and guardar != "N":
                                
                print("=======================================")
                print("\n")
                print("Error: Opción inválida. Intenta de nuevo.")
                print("\n")
                print("=======================================")
                print("\n")

                guardar = input("¿Desea guardar el reporte por categoria en un archivo externo?[Y/N]: ")
                guardar = guardar.capitalize()    
                print("\n")
            
            if guardar == "Y":
                
                archivoExterno = input("Ingrese el nombre del archivo: ")
                archivo = open(archivoExterno + ".txt", encoding="utf-8", mode="a")
                archivo.write("..........................................................................\n")
                archivo.write("                       REPORTE POR CATEGORIA                              \n")
                archivo.write(f"Reporte generado el {fechaActual}\n\t\t\t\t\t{horaActual}\n")
                archivo.write(f"Categoria: {categoriaEncontrada}\n")
                archivo.write("Código\tProducto\tPrecio Unitario\t\tCantidad\n")
                for linea in nuevasLineas:
                    archivo.write(linea)
                archivo.write("\n..........................................................................\n\n")
                archivo.close()
                print("\n")
                print("El reporte por categoria ha sido guardado exitosamente.")
                return ReportesInventario()
            
            else:
                print("\n")
                print("Reporte por categoria finalizado")
                return ReportesInventario()
    
        else:
            print("Aún no haz realizado ningún registro de inventario.")
            print("Te vamos a redireccionar al aparatado de 'inventario'")
            print("para que realices los registros correspodientes.")
            return inventario()
    else:
        print("Error: El parámetro de entrada no debe ser vacio")
        return reportesCategoria()
    
"--------------------------------------------------------------------------------"

"""
Nombre: reportesExistencia
Entrada: --
Salida: Devuelve el contenido del inventario, solo si la cantidad de este
        es mayor a cero.
Restricciones: --
"""

def reportesExistencia():
    
    print("\n")
    print("=======================================")
    print("\n")
    print("         Reporte por Existencia        ")
    print("\n")
    print("=======================================")
    print("\n")
    
    fechaActual = datetime.date.today().strftime("%d/%m/%Y")
    horaActual = datetime.datetime.now().strftime("%I:%M:%p")
    nuevasLineas = []
    
    archivo = open ("Inventario.txt", encoding = "utf-8", mode = "r")
    contenido = archivo.readlines()
    archivo.close()

    if largoTexto_Aux(contenido) != 0:
        for linea in contenido:
            contenido = linea.strip().split(';')
            cantidad = int(contenido[4])
            
            if cantidad > 0:
                codigo = contenido[0] 
                producto = contenido[1]  
                precioUnitario = contenido[3]

                nuevaLinea = f"{codigo}\t\t{producto}\t\t\t{precioUnitario}₡\t\t\t{cantidad}\n"
                nuevasLineas += [nuevaLinea]
                
        print(".......................................")
        print("           Inicio Reporte              ")
        print(".......................................")
        print("\n")
        print("Código\t\tProducto\t\tPrecio Unitario\t\tCantidad")
        print("\n")
        for linea in nuevasLineas:
                print(linea)
        print("\n")
        print(".......................................")
        print("              Fin Reporte              ")
        print(".......................................")
        print("\n")
        print("=======================================")

        guardar = input("¿Desea guardar el reporte por existencia en un archivo externo?[Y/N]: ")
        guardar = guardar.capitalize()    
        print("\n")
            
        while guardar != "Y" and guardar != "N":
                            
            print("=======================================")
            print("\n")
            print("Error: Opción inválida. Intenta de nuevo.")
            print("\n")
            print("=======================================")
            print("\n")

            guardar = input("¿Desea guardar el reporte por existencia en un archivo externo?[Y/N]: ")
            guardar = guardar.capitalize()    
            print("\n")
            
        if guardar == "Y":
                
            archivoExterno = input("Ingrese el nombre del archivo: ")
            archivo = open(archivoExterno + ".txt", encoding="utf-8", mode="a")
            archivo.write("..........................................................................\n")
            archivo.write("                       REPORTE POR EXISTENCIA                             \n")
            archivo.write(f"Reporte generado el {fechaActual}\n\t\t\t\t\t{horaActual}\n")
            archivo.write("Código\tProducto\tPrecio Unitario\t\tCantidad\n")
            for linea in nuevasLineas:
                archivo.write(linea)
            archivo.write("\n..........................................................................\n\n")
            archivo.close()
            print("\n")
            print("El reporte por existencia ha sido guardado exitosamente.")
            return ReportesInventario()
            
        else:
            print("\n")
            print("Reporte por existencia finalizado")
            return ReportesInventario()
    
    else:
        print("Aún no haz realizado ningún registro de inventario.")
        print("Te vamos a redireccionar al aparatado de 'inventario'")
        print("para que realices los registros correspodientes.")
        return inventario()
    
"--------------------------------------------------------------------------------"
"--------------------------------------------------------------------------------"    

"""
Nombre: facturar
Entrada: código y cantidad
Salidad: Mostar en pantalla el formato de facturación con la información
         de esta.
Restricciones:
             ¬ El código debe ser existente y valido.
             ¬ La cantidad ingresada debe ser menor o igual a la existente.
"""

def facturar():
    
    print("\n")
    print("=======================================")
    print("\n")
    print("               Facturación             ")
    print("\n")
    print("=======================================")
    print("\n")

    numFactura = numFactura_Aux()

    cliente = cliente_Aux()
    print(f"Facturación en proceso para el/la cliente {cliente}") 
    print("\n")
    mostrar = mostrar_Aux()
    print("\n")

    fechaActual = datetime.date.today().strftime("%d/%m/%Y")
    horaActual = datetime.datetime.now().strftime("%I:%M:%p")
    pago = ""

    productos = []
    nuevasLineas = [] 
    subTotal = 0
    impuestos = 0
    Total = 0

    empezar = True
    while empezar:

        codigoIngresado = codigoIngresado_Aux()
            
        archivo = open("Inventario.txt", encoding="utf-8", mode="r")
        lineas = archivo.readlines()
        archivo.close()

        encontrado = False

        for linea in lineas:
                
            contenido = linea.split(";")
            codigoLinea = int(contenido[0])
                
            if codigoIngresado == codigoLinea:
                encontrado = True
                    
                producto = contenido[1]
                categoria = contenido[2]
                cantidad = int(contenido[4]) 

                print("=======================================")
                print("\n")
                print(f"El producto registrado con código {codigoIngresado} es {producto}")
                print(f"la cantidad en inventario es de {cantidad} unidades")
                print("\n")
                print("=======================================")
                print("\n")

                cantidadComprar = cantidadComprar_Aux(cantidad)

                nuevoInventario = nuevoInventario_Aux(cantidadComprar, codigoIngresado)       
                
                precioUnitario = int(contenido[3])
                impuesto = (precioUnitario * 0.13) * cantidadComprar
                subtotal = (precioUnitario * cantidadComprar)
                total = (precioUnitario*cantidadComprar) + impuesto
                      
                compra = f"{cantidadComprar}\t\t{producto}\t\t{precioUnitario}\t\t\t{impuesto}\t\t{total}"
                productos += [compra]

                print("=======================================")
                print("\n")
                print("Cantidad\tProducto\tPrecio Unitario\t\tImpuesto\tTotal")
                for linea in productos:
                    print(linea)
                print("\n")
                print("=======================================")
                print("\n")

                subTotal += subtotal
                impuestos += impuesto
                Total += total

                facturaDetalle = facturasDetalle_AUX(numFactura, codigoIngresado, producto, cantidadComprar, precioUnitario, subtotal,impuesto,total)

                opcion = input("¿Quieres realizar otra compra?[Y/N]: ")
                opcion = opcion.capitalize()
                print("\n") 

                while opcion != "Y" and opcion != "N":
                    
                    print("=======================================")
                    print("\n")
                    print("Error: Opción inválida. Intenta de nuevo.")
                    print("\n")
                    print("=======================================")
                    print("\n")
                    
                    opcion = input("¿Quieres realizar otra compra?[Y/N]: ")
                    print("\n")
                    opcion = opcion.capitalize()
                    
                if opcion == "Y":
                    continue
                elif opcion == "N":
                    empezar = False
                    
    if encontrado == True:

        factura = facturas_Aux(numFactura,cliente,fechaActual,horaActual,subTotal,impuestos,Total,pago)
            
        print("=======================================")
        print("\n")
        print(f"Factura {numFactura}")
        print(f"Fecha: {fechaActual}\t\t\t\t\tHora: {horaActual}")
        print(f"Cliente: {cliente}")
        print("Cantidad\tProducto\tPrecio Unitario\t\tImpuesto\tTotal")
        for linea in productos:
            print(linea)
        print("\n")
        print(f"Sub total: {subTotal}")
        print(f"Impuestos: {impuestos}")
        print(f"Total: {Total}")
        print("\n")
        print("=======================================")
        print("\n")
        return menu()
                        
    else:
        print("=======================================")
        print("\n")
        print(f"El código {codigoIngresado} no fue encontrado en el inventario.")
        print("\n")
        print("=======================================")
        print("\n")
            
"--------------------------------------------------------------------------------"
"--------------------------------------------------------------------------------"

"""
Nombre: reportes
Entrada: opcion
Salida: Direccionar al usuario a la opción seleccionada
Restricciones:
             ¬ La opción no debe ser vacia
             ¬ La opción debe estar en el parámetro mostrado
"""

def reportes():
    
    print("\n")
    print("=======================================")
    print("\n")
    print("             Menú Reportes             ")
    print("\n")
    print("=======================================")
    print("\n")
    print("Opciones:")
    print("       RF: Reporte de facturas")
    print("\n")
    print("       RP: Reporte por productos vendidos")
    print("\n")
    print("       RC: Reporte por clientes")
    print("\n")
    print("       RFC: Reporte por fechas")
    print("\n")
    print("       E: Estado de utilidades")
    print("\n")
    print("       M: Volver al menú principal")
    print("\n")
    print("       S: Salir")
    print("\n")

    opcion = input("Ingrese la opción deseada: ")
    opcion = opcion.upper()
    print("\n")

    if (opcion != ""):
                
        if opcion == "RF":
            return reporteFacturas()
            
        elif opcion == "RP":
            return reporteProductos()
            
        elif opcion == "RC":
            return reporteClientes()

        elif opcion == "RFC":
            return reporteFechas()

        elif opcion == "E":
            return estadoUtilidades()
        
        elif opcion == "M":
            return menu()
        
        elif opcion == "S":
            return salir()
            
        else:
            print("=======================================")
            print("\n")
            print("Error: Opción no reconocida")
            return reportes()
    else:
        print("=======================================")
        print("\n")
        print("Error: El parámetro de entrada no debe ser vacio")
        return reportes() 


"--------------------------------------------------------------------------------"

"""
Nombre: reporteFacturas
Entrada: (nombre de un archivo .txt en caso de que el usuario desee guardar
          el reporte en un archivo externo)
Salida: Devuelve los reportes según el formato indicado 
Restricciones: (nombre del archivo .txt no debe ser vacio)
"""

def reporteFacturas():

    print("\n")
    print("=======================================")
    print("\n")
    print("         Reporte de Facturas           ")
    print("\n")
    print("=======================================")
    print("\n")
    
    archivo = open ("Facturas.txt", encoding = "utf-8", mode = "r")
    lineas = archivo.readlines()
    archivo.close()
    fechaActual = datetime.date.today().strftime("%d/%m/%Y")
    horaActual = datetime.datetime.now().strftime("%I:%M:%p")
    nuevasLineas = []
    Total = 0
    
    if largoTexto_Aux(lineas) != 0:
        
        print(".......................................")
        print("           Inicio Reporte              ")
        print(".......................................")
        print("\n")
        
        for linea in lineas:
            
            contenido = linea.split(',')
            factura = contenido[0]
            fecha = contenido[2]
            cliente = contenido[1]
            totalFacturado = float(contenido[6])
            Total += totalFacturado 

            nuevaLinea = f"{factura}\t\t{fecha}\t\t{cliente}\t\t{totalFacturado}\n"
            nuevasLineas += [nuevaLinea]
            
        print("\n")
        print("Factura\t\tFecha\t\t\tCliente\t\t\tTotal Facturado")
        print("\n")
        for linea in nuevasLineas:
            print(linea)
        print("\n")
        print(f"\t\t\t\t\t\t\tTotal: {Total}")
        print("\n")
        print(".......................................")
        print("              Fin Reporte              ")
        print(".......................................")
        print("\n")
        print("=======================================")
        print("\n")
        
        guardar = input("¿Desea guardar el reporte de facturas en un archivo externo?[Y/N]: ")
        guardar = guardar.capitalize()
        print("\n")

        while guardar != "Y" and guardar != "N":
                    
            print("=======================================")
            print("\n")
            print("Error: Opción inválida. Intenta de nuevo.")
            print("\n")
            print("=======================================")
            print("\n")

            guardar = input("¿Desea guardar el reporte de facturas en un archivo externo?[Y/N]: ")
            guardar = guardar.capitalize()    
            print("\n")
            
        if guardar == "Y":
            
            archivoExterno = input("Ingrese el nombre del archivo: ")
            archivo = open(archivoExterno + ".txt", encoding="utf-8", mode="w")
            archivo.write(f"Reporte generado el {fechaActual}\n\t\t\t\t\t{horaActual}\n")
            archivo.write("\nFactura\t\tFecha\t\t\tCliente\t\t\tTotal Facturado\n\n")
            for linea in nuevasLineas:
                archivo.write(linea)
            archivo.write(f"\n\t\t\t\t\t\t\t\t\t Total: {Total}\n")
            archivo.close()
            print("\n")
            print("El reporte por facturas ha sido guardado exitosamente.")
            return reportes()
        else:
            print("\n")
            print("Reporte por facturas finalizado")
            return reportes()
    else:
        print("\n")
        print("Aún no haz realizado ningún registro de inventario.")
        print("Te vamos a redireccionar al aparatado de 'inventario'")
        print("para que realices los registros correspodientes.")
        return inventario()
    

"--------------------------------------------------------------------------------"

"""
Nombre: reporteProductos
Entrada: (nombre de un archivo .txt en caso de que el usuario desee guardar
          el reporte en un archivo externo)
Salida: Devuelve los reportes según el formato indicado 
Restricciones: (nombre del archivo .txt no debe ser vacio)
"""

def reporteProductos():

    print("\n")
    print("=======================================")
    print("\n")
    print("    Reporte por productos vendidos     ")
    print("\n")
    print("=======================================")
    print("\n")

    productoBuscar = input("Ingrese el nombre del producto por buscar: ")
    productoBuscar = productoBuscar.capitalize()
    print("\n")
    
    archivoF = open ("Facturas.txt", encoding = "utf-8", mode = "r")
    lineasF = archivoF.readlines()
    archivoF.close()
    
    archivoFD = open ("FacturasDetalle.txt", encoding = "utf-8", mode = "r")
    lineasFD = archivoFD.readlines()
    archivoFD.close()
    
    fechaActual = datetime.date.today().strftime("%d/%m/%Y")
    horaActual = datetime.datetime.now().strftime("%I:%M:%p")
    nuevasLineas = []
    Total = 0
    
    if largoTexto_Aux(lineasF) != 0 and largoTexto_Aux(lineasFD) != 0:

        largoProductoBuscar = largoTexto_Aux(productoBuscar)
        encontrado = False
        
        print(".......................................")
        print("           Inicio Reporte              ")
        print(".......................................")
        print("\n")
        
        for lineaFD in lineasFD:
            
            contenidoFD = lineaFD.split(',')
            
            facturaFD = contenidoFD[0]
            producto = contenidoFD[2]
            precioUnitario = float(contenidoFD[4])
            cantidad = contenidoFD[3]
            impuesto = float(contenidoFD[6])
            totalFacturado = float(contenidoFD[7])

            productoCorte = producto[0:largoProductoBuscar]

            if productoBuscar == productoCorte:
                encontrado = True
                Total += totalFacturado 
                
                for lineaF in lineasF:
                    contenidoF = lineaF.split(',')
                    facturaF = contenidoF[0]
                    fechaF = contenidoF[2]

                    if facturaFD == facturaF:
                
                        nuevaLinea = f"{facturaFD}\t\t{fechaF}\t{precioUnitario}\t\t\t{cantidad}\t\t{impuesto}\t\t{totalFacturado}\n"
                        nuevasLineas += [nuevaLinea]
                        productoEncontrado = producto

        if encontrado == False:
            print("Error: producto no reconocido")
            return reporteProductos()
        
        print("\n")
        print(f"Producto: {productoEncontrado}")
        print("Factura\t\tFecha\t\tPrecio Unitario\t\tCantidad\tImpuesto\tTotal Facturado")
        print("\n")
        for linea in nuevasLineas:
            print(linea)
        print("\n")
        print(f"\t\t\t\t\t\t\t\t\t\t Total: {Total}")
        print("\n")
        print(".......................................")
        print("              Fin Reporte              ")
        print(".......................................")
        print("\n")
        print("=======================================")
        print("\n")

        
        guardar = input("¿Desea guardar el reporte por productos vendidos en un archivo externo?[Y/N]: ")
        guardar = guardar.capitalize()
        print("\n")

        while guardar != "Y" and guardar != "N":
                    
            print("=======================================")
            print("\n")
            print("Error: Opción inválida. Intenta de nuevo.")
            print("\n")
            print("=======================================")
            print("\n")

            guardar = input("¿Desea guardar el reporte por productos vendidos en un archivo externo?[Y/N]: ")
            guardar = guardar.capitalize()    
            print("\n")
            
        if guardar == "Y":
            
            archivoExterno = input("Ingrese el nombre del archivo: ")
            archivo = open(archivoExterno + ".txt", encoding="utf-8", mode="a")
            archivo.write("..........................................................................\n")
            archivo.write(f"Reporte generado el {fechaActual}\n\t\t\t\t\t{horaActual}\n")
            archivo.write(f"Producto: {productoEncontrado}\n")
            archivo.write("Factura\tFecha\t\tPrecio\t\tCantidad\tImpuesto\tTotal Facturado\n")
            for linea in nuevasLineas:
                archivo.write(linea)
            archivo.write(f"\t\t\t\t\t\t\t\t\t\t\t\t Total: {Total}\n")
            archivo.write("..........................................................................\n\n")
            archivo.close()
            print("\n")
            print("El reporte por productos vendidos ha sido guardado exitosamente.")
            return reportes()
        else:
            print("\n")
            print("Reporte por productos vendidos finalizado")
            return reportes()
        
    else:
        print("\n")
        print("Aún no haz realizado ningún registro de inventario.")
        print("Te vamos a redireccionar al aparatado de 'inventario'")
        print("para que realices los registros correspodientes.")
        return inventario()

"--------------------------------------------------------------------------------"

"""
Nombre: reporteClientes
Entrada: (nombre de un archivo .txt en caso de que el usuario desee guardar
          el reporte en un archivo externo)
Salida: Devuelve los reportes según el formato indicado 
Restricciones: (nombre del archivo .txt no debe ser vacio)
"""

def reporteClientes():

    print("\n")
    print("=======================================")
    print("\n")
    print("         Reporte por Clientes          ")
    print("\n")
    print("=======================================")
    print("\n")

    clienteBuscar = input("Ingrese el nombre del cliente por buscar: ")
    clienteBuscar = clienteBuscar.capitalize()
    print("\n")
    
    archivo = open ("Facturas.txt", encoding = "utf-8", mode = "r")
    lineas = archivo.readlines()
    archivo.close()
    
    fechaActual = datetime.date.today().strftime("%d/%m/%Y")
    horaActual = datetime.datetime.now().strftime("%I:%M:%p")
    nuevasLineas = []
    Total = 0
    
    if largoTexto_Aux(lineas) != 0:

        largoClienteBuscar = largoTexto_Aux(clienteBuscar)
        encontrado = False
        
        print(".......................................")
        print("           Inicio Reporte              ")
        print(".......................................")
        print("\n")
        
        for linea in lineas:
            
            contenido = linea.split(',')
            
            factura = contenido[0]
            cliente = contenido[1]
            fecha = contenido[3]
            totalFacturado = float(contenido[6])

            clienteCorte = cliente[0:largoClienteBuscar]

            if clienteBuscar == clienteCorte:
                encontrado = True  
                clienteEncontrado = cliente
                Total += totalFacturado 
                nuevaLinea = f"{factura}\t\t\t{fecha}\t{totalFacturado}\n"
                nuevasLineas += [nuevaLinea]

        if encontrado == False:
            print("Error: cliente no reconocido")
            return reporteClientes()
        
        print("\n")
        print(f"Cliente: {clienteEncontrado}")
        print("Factura\t\t\tFecha\t\tTotal Facturado")
        print("\n")
        for linea in nuevasLineas:
            print(linea)
        print("\n")
        print(f"\t\t\t\t Total: {Total}")
        print("\n")
        print(".......................................")
        print("              Fin Reporte              ")
        print(".......................................")
        print("\n")
        print("=======================================")
        print("\n")

        
        guardar = input("¿Desea guardar el reporte por cliente en un archivo externo?[Y/N]: ")
        guardar = guardar.capitalize()
        print("\n")

        while guardar != "Y" and guardar != "N":
                    
            print("=======================================")
            print("\n")
            print("Error: Opción inválida. Intenta de nuevo.")
            print("\n")
            print("=======================================")
            print("\n")

            guardar = input("¿Desea guardar el reporte por cliente en un archivo externo?[Y/N]: ")
            guardar = guardar.capitalize()    
            print("\n")
            
        if guardar == "Y":
            
            archivoExterno = input("Ingrese el nombre del archivo: ")
            archivo = open(archivoExterno + ".txt", encoding="utf-8", mode="a")
            archivo.write("..........................................................................\n")
            archivo.write(f"Reporte generado el {fechaActual}\n\t\t\t\t\t{horaActual}\n")
            archivo.write(f"Cliente: {clienteEncontrado}\n")
            archivo.write("Factura\t\tFecha\t\tTotal Facturado\n\n")
            for linea in nuevasLineas:
                archivo.write(linea)
            archivo.write(f"\t\t\t\t Total: {Total}\n")
            archivo.write("..........................................................................\n\n")
            archivo.close()
            print("\n")
            print("El reporte por cliente ha sido guardado exitosamente.")
            return reportes()
        else:
            print("\n")
            print("Reporte por cliente finalizado")
            return reportes()
        
    else:
        print("\n")
        print("Aún no haz realizado ningún registro de inventario.")
        print("Te vamos a redireccionar al aparatado de 'inventario'")
        print("para que realices los registros correspodientes.")
        return inventario()

"--------------------------------------------------------------------------------"

"""
Nombre: reporteClientes
Entrada: Rango de fechas, (nombre de un archivo .txt en caso de que el usuario desee guardar
          el reporte en un archivo externo)
Salida: Devuelve los reportes según el formato indicado 
Restricciones: Formato de fechas valido, (nombre del archivo .txt no debe ser vacio)
"""

def reporteFechas():

    print("\n")
    print("=======================================")
    print("\n")
    print("         Reporte por Fechas            ")
    print("\n")
    print("=======================================")
    print("\n")

    fechaInicio = input("Ingrese la fecha inicial: ")
    fechaFinal = input("Ingrese la fecha final: ")
    nuevasLineas = []
    Total = 0

    fechaActual = datetime.date.today().strftime("%d/%m/%Y")
    horaActual = datetime.datetime.now().strftime("%I:%M:%p")
    
    archivo = open("Facturas.txt", encoding="utf-8", mode="r")
    lineas = archivo.readlines()
    archivo.close()

    if largoTexto_Aux(lineas) != 0:
        if (fechaInicio != "") and (fechaFinal != ""):
                
                try:
                    fechaInicio = datetime.datetime.strptime(fechaInicio, '%d/%m/%Y')
                    fechaFinal = datetime.datetime.strptime(fechaFinal, '%d/%m/%Y')
                except:
                    print("Error: Las fechas deben tener el formato dd/mm/yyyy.")
                    return reporteFechas()
                else:
                    
                    encontrado = False
            
                    print(".......................................")
                    print("           Inicio Reporte              ")
                    print(".......................................")
                    print("\n")
            
                    for linea in lineas:
                    
                        contenido = linea.strip().split(",")
                        fechas = datetime.datetime.strptime(contenido[2], '%d/%m/%Y')
                    
                        if fechaInicio <= fechas <= fechaFinal:
                            encontrado = True
                            
                            factura = contenido[0]
                            cliente = contenido[1]
                            subTotal = float(contenido[4])
                            Impuestos = float(contenido[5])
                            total = float(contenido[6])
                            pago = contenido[7]
                            Total += total
                            
                            nuevaLinea = f"{factura}\t\t{cliente}\t{subTotal}\t\t{Impuestos}\t\t{total}\t{pago}\n"
                            nuevasLineas += [nuevaLinea]
                    
                    if encontrado == False:
                        print("Error: rango de fechas no reconocido")
                        return reporteFechas()
                    
                    print("\n")
                    print("Factura\t\tCliente\t\tSub Total\tImpuestos\tTotal\t\tForma de pago")
                    print("\n")
                    for linea in nuevasLineas:
                        print(linea)
                    print("\n")
                    print(f"\t\t\t\t\t\t\t Total: {Total}")
                    print("\n")
                    print(".......................................")
                    print("              Fin Reporte              ")
                    print(".......................................")
                    print("\n")
                    print("=======================================")
                    print("\n")

                    
                    guardar = input("¿Desea guardar el reporte por rango de fechas en un archivo externo?[Y/N]: ")
                    guardar = guardar.capitalize()
                    print("\n")

                    while guardar != "Y" and guardar != "N":
                                
                        print("=======================================")
                        print("\n")
                        print("Error: Opción inválida. Intenta de nuevo.")
                        print("\n")
                        print("=======================================")
                        print("\n")

                        guardar = input("¿Desea guardar el reporte por rango de fechas en un archivo externo?[Y/N]: ")
                        guardar = guardar.capitalize()    
                        print("\n")
                        
                    if guardar == "Y":
                        
                        archivoExterno = input("Ingrese el nombre del archivo: ")
                        archivo = open(archivoExterno + ".txt", encoding="utf-8", mode="a")
                        archivo.write("..........................................................................\n")
                        archivo.write(f"Reporte generado el {fechaActual}\n\t\t\t\t\t{horaActual}\n")
                        archivo.write("Factura\t\tCliente\t\tSub Total\tImpuestos\tTotal\t\tForma de pago\n")
                        for linea in nuevasLineas:
                            archivo.write(linea)
                        archivo.write(f"\t\t\t\t\t\t\t\t\t\t Total: {Total}\n")
                        archivo.write("..........................................................................\n\n")
                        archivo.close()
                        print("\n")
                        print("El reporte por rango de fechas ha sido guardado exitosamente.")
                        return reportes()
                    else:
                        print("\n")
                        print("Reporte por rango de fechas finalizado")
                        return reportes()        
    else:
        print("\n")
        print("Aún no haz realizado ningún registro de inventario.")
        print("Te vamos a redireccionar al aparatado de 'inventario'")
        print("para que realices los registros correspodientes.")
        return inventario()

"--------------------------------------------------------------------------------"
"--------------------------------------------------------------------------------"

"""
Nombre: estadoUtilidades
Entrada: --
Salida: 
       Retornar:
                • Total Facturas
                • Cantidad de productos facturados únicos
                • SubTotal Facturado 
                • Total Impuesto
                • Total Facturado
Restricciones: --
"""

def estadoUtilidades():
    print("\n")
    print("=======================================")
    print("\n")
    print("          Estado de Utilidades         ")
    print("\n")
    print("=======================================")
    print("\n")

    archivo = open("FacturasDetalle.txt", encoding="utf-8", mode="r")
    lineas = archivo.readlines()
    archivo.close()

    TotalFacturas = 0 
    subTotalFacturado = 0
    impuestoFacturado = 0
    totalFacturado = 0
    productosFacturadosUnicos = 0
    productosFacturados = []

    if largoTexto_Aux(lineas) != 0:
        for linea in lineas:
            
            if linea != "":
                TotalFacturas += 1

        for linea in lineas:
            contenido = linea.strip().split(",")
            producto = contenido[2]

            repetido = False
            for productoF in productosFacturados:
                if productoF == producto:
                    repetido = True
                    break
            if not repetido:
                productosFacturadosUnicos += 1
                productosFacturados += [producto]

        for linea in lineas:
            contenido = linea.strip().split(",")
            subTotal = float(contenido[5])
            impuesto = float(contenido[6])
            total = float(contenido[7])
            subTotalFacturado += subTotal
            totalFacturado += total
            impuestoFacturado += impuesto 

        print("\n+-----------------------------------------------------------------+\n")     
        print(f" ¬ Total de facturas: {TotalFacturas}\n")
        print(f" ¬ Cantidad de productos facturados únicos: {productosFacturadosUnicos}\n")
        print(f" ¬ SubTotal facturado: {subTotalFacturado}\n")
        print(f" ¬ Total de impuesto facturado: {impuestoFacturado}\n")
        print(f" ¬ Total facturado: {totalFacturado}\n")
        print("+-----------------------------------------------------------------+")  

        return reportes()
    
    else:
        print("\n")
        print("Aún no haz realizado ningún registro de inventario.")
        print("Te vamos a redireccionar al aparatado de 'inventario'")
        print("para que realices los registros correspodientes.")

"--------------------------------------------------------------------------------"
"--------------------------------------------------------------------------------"

def salir():
    print("\n+-----------------------------------------------------------------+\n")  
    print("          Haz cerrado exitosamente tu gestor negocio                 ")
    print("\n+-----------------------------------------------------------------+\n")  

"--------------------------------------------------------------------------------"
"--------------------------------------------------------------------------------"

## Función para determinar el largo de un texto

def largoTexto_Aux(texto):
    
    contador = 0
    
    for letra in texto:
        contador += 1
        
    return contador

"--------------------------------------------------------------------------------"

## Función para generar el código automáticamente

def codigo_Aux():
    
    archivo = open("Inventario.txt", encoding="utf-8", mode = 'r')
    lineas = archivo.readlines()
    archivo.close()

    if largoTexto_Aux(lineas) == 0:
        nuevoCodigo = 1
        
    else:

        for linea in lineas:
            if linea.strip():        
                codigo = linea.split(';')[0].strip()
                nuevoCodigo = int(codigo) + 1
        
    return nuevoCodigo

"--------------------------------------------------------------------------------"

## Función para pedir el nombre del cliente

def cliente_Aux():

    cliente = ""
    while cliente == "":
        cliente = input('Por favor, ingrese el nombre del cliente: ')
        print("\n")
        
        if cliente == "":
            print("=======================================")
            print("\n")
            print("Error: El parámetro de entrada no debe ser vacio. Inténtelo de nuevo.")
            print("\n")
            print("=======================================")
            print("\n")

    return cliente

"--------------------------------------------------------------------------------"

## Función para preguntar si se quiere visualizar el contenido del inventario o no

def mostrar_Aux():

    while True:
        opcion = input("¿Quieres que se muestre el contenido de tu inventario (Y/N)?: ")
        opcion = opcion.capitalize()
        print()

        if opcion == "Y":
            archivo = open("Inventario.txt", encoding="utf-8", mode="r")
            lineas = archivo.readlines()
            archivo.close()

            if largoTexto_Aux(lineas) != 0:
                print("========================================")
                print("\n")
                for linea in lineas:
                    cantidad = int(linea.strip().split(';')[4])
                    if cantidad != 0:
                        print(linea)
                print("========================================")
                print("\n")
            else:
                print("========================================")
                print("\n")
                print("Aún no has registrado ningún inventario, te vamos a redireccionar")
                print("al menú 'inventario' para que realices los registros pertimentes.")
                print("\n")
                print("========================================")
                print("\n")
                return inventario()

            break

        elif opcion == "N":
            break

        else:
            print("=======================================")
            print("\n")
            print("Error: opción no reconocida. Por favor ingrese 'Y' o 'N'")
            print("\n")
            print("=======================================")
            print("\n")

def mostrar_Auxi():

    while True:
        opcion = input("¿Quieres que se muestre el contenido de tu inventario (Y/N)?: ")
        opcion = opcion.capitalize()
        print()

        if opcion == "Y":
            archivo = open("Inventario.txt", encoding="utf-8", mode="r")
            lineas = archivo.readlines()
            archivo.close()

            if largoTexto_Aux(lineas) != 0:
                print("========================================")
                print("\n")
                for linea in lineas:
                        print(linea)
                print("========================================")
                print("\n")
            else:
                print("========================================")
                print("\n")
                print("Aún no has registrado ningún inventario, te vamos a redireccionar")
                print("al menú 'inventario' para que realices los registros pertimentes.")
                print("\n")
                print("========================================")
                print("\n")
                return inventario()

            break

        elif opcion == "N":
            break

        else:
            print("=======================================")
            print("\n")
            print("Error: opción no reconocida. Por favor ingrese 'Y' o 'N'")
            print("\n")
            print("=======================================")
            print("\n")
            
"--------------------------------------------------------------------------------"

## Función para pedir el codigo 

def codigoIngresado_Aux():

    while True:

        codigoIngresado = input("Digite el código del inventario para agregar a la factura: ")
        print("\n")

        if codigoIngresado == "":
            print("=======================================")
            print("\n")        
            print("Error: El código no debe ser vacío")
            print("\n")
            print("=======================================")
            print("\n")
            continue
        
        try:
            codigoIngresado = int(codigoIngresado)
        except:
            print("=======================================")
            print("\n")
            print("Error: El código ingresado debe ser numérico")
            print("\n")
            print("=======================================")
            print("\n")
            continue
        
        return codigoIngresado
    
"--------------------------------------------------------------------------------"

## Función para pedir la cantidad

def cantidadComprar_Aux(cantidad):

    while True:

        cantidadComprar = (input("Digite la cantidad que deseas facturar del producto: "))
        print("\n")

        if cantidadComprar == "":
            print("=======================================")
            print("\n")        
            print("Error: El parámetro de entrada no debe ser vacío")
            print("\n")
            print("=======================================")
            print("\n")
            continue
        
        try:
            cantidadComprar = int(cantidadComprar)
        except:
            print("=======================================")
            print("\n")
            print("Error: La cantidad ingreseda debe ser númerica")
            print("\n")
            print("=======================================")
            print("\n")
            continue
        
        if cantidadComprar > cantidad:
            print("=======================================")
            print("\n")
            print("Error: La cantidad ingresada excede a la cantidad en inventario, por favor verifique el inventario antes de comprar.")
            print("\n")
            print("=======================================")
            continue
        
        if cantidadComprar == 0:
            print("=======================================")
            print("\n")
            print("Error: La cantidad no puede ser 0.")
            print("\n")
            print("=======================================")
            continue
        
        return cantidadComprar
                        
"--------------------------------------------------------------------------------"

## Función para generar el numero de factura automáticamente

def numFactura_Aux():
    
    archivo = open("NumFactura.txt", 'r')
    lineas = archivo.readlines()
    archivo.close()

    if largoTexto_Aux(lineas) == 0:
        numFactura = 1

    else:
        for linea in lineas:
            if linea.strip():
                numFactura = linea.split(';')[0].strip()
                numFactura = int(numFactura) + 1
        
    archivo = open("NumFactura.txt",'a')
    lineas = archivo.write(f"{numFactura}\n")
    archivo.close()
    
    return numFactura

"--------------------------------------------------------------------------------"

## Función para registrar las facturas

def facturasDetalle_AUX(numFactura, codigo, producto, cantidadComprar, precioUnitario, subtotal,impuesto,total):
        
        facturaDetalle = f"{numFactura},{codigo},{producto},{cantidadComprar},{precioUnitario},{subtotal},{impuesto},{total}\n"
        archivo = open("FacturasDetalle.txt",encoding="utf-8", mode = 'a')
        archivo.writelines(facturaDetalle)
        archivo.close()
    
"--------------------------------------------------------------------------------"

## Función para registrar las facturas

def facturas_Aux(numFactura,cliente,fechaActual,horaActual,subTotal,impuestos,Total,pago):
    
    pago = input("Ingrese la forma de pago: ")
    if pago == "":
        print("Error: El parámetro de entrada no debe ser vacio")
        return facturas_Aux(numFactura,cliente,fechaActual,horaActual,subTotal,impuestos,Total,pago)
    else:
        factura = f"{numFactura},{cliente},{fechaActual},{horaActual},{subTotal},{impuestos},{Total},{pago}\n"
        archivo = open("Facturas.txt",encoding="utf-8", mode = 'a')
        archivo.writelines(factura)
        archivo.close()

"--------------------------------------------------------------------------------"

## Función para borrar la cantidad facturada del inventario

def nuevoInventario_Aux(cantidadComprar, codigoIngresado):
    
    nuevasLineas = []
    nuevaLinea = ""
    
    archivo = open("Inventario.txt", encoding="utf-8", mode="r")
    lineas = archivo.readlines()
    archivo.close()
    
    for linea in lineas:
        
        contenido = linea.split(";")       

        if int(codigoIngresado) == int(contenido[0]):
            
            cantidad = ""
            for caracter in contenido[4]:
                if caracter == "\n":
                    break
                cantidad += caracter
            nuevaCantidad = int(cantidad) - int(cantidadComprar)
            nuevaLinea = f"{contenido[0]};{contenido[1]};{contenido[2]};{contenido[3]};{nuevaCantidad}\n"

            nuevasLineas += [nuevaLinea]
        else:
            nuevasLineas += [linea]
            
    archivo = open("Inventario.txt", encoding="utf-8", mode="w")
    archivo.writelines(nuevasLineas)
    archivo.close()

"--------------------------------------------------------------------------------"
menu()
