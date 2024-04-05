import os
vehiculo = []
repuestos = []
mano_obra = []
mantenimiento = []
#BUSCAR LOS DATOS DE CADA GESTION
def guardarDato(archivo,tabla):
    if not isinstance(archivo,str):
        print("Error: Tipo de parámetro no es texto.")
    if (archivo == ""):
        print( "Error: El nombre del archivo no debe ser vacio")

    if not os.path.exists(archivo+'.txt'):

        print (f"Error: El archivo '{archivo}' no existe")
    
    abrir = open(archivo+".txt", encoding= "utf-8", mode= "r+")
    for fila in tabla:
        abrir.write(str(fila[0]))
        for elemento in fila[1:]:
            abrir.write(',' + str(elemento))
        abrir.write('\n')
    abrir.close()
#MODIFICA LOS DATOS DE CADA GESTIÓN
def modificarDato(archivo):
    if not isinstance(archivo,str):
            print("Error: Tipo de parámetro no es texto.")
    if (archivo == ""):
        print( "Error: El nombre del archivo no debe ser vacio")

    if not os.path.exists(archivo+'.txt'):

         print (f"Error: El archivo '{archivo}' no existe")
    archivo = open(archivo +".txt", encoding= "utf-8", mode= "w")
    dato = input("Ingrese el dato que desea modificar ") 
    
#CARGA EL DATO DE CAFA GESTIÓN.
def cargarDato(archivo):
    if not isinstance(archivo,str):
        return "Error: Tipo de parámetro no es texto."
    if (archivo == ""):
        return "Error: El nombre del archivo no debe ser vacio"
    if not os.path.exists(archivo + ".txt"):
        return f"Error: El archivo '{archivo}' no existe"
      
    abrir = open(archivo + ".txt", encoding = "utf-8", mode = "r")
    lista = abrir.readlines()
    for linea in lista:
        linea = linea[:-1].split(',')
        vehiculo.append(linea)
    print(vehiculo)
#MUESTRA LO QUE HAY DENTRO DE CADA GESTIÓN DE ARCHIVO    
def tablaMostrar(tabla):
    for linea in tabla:
        print(linea)

###########################
#FUNCIONES DE ADMINISTRADOR
###########################
          
#AGREGAR TIPOS DE GESTIÓN
def agregarVehiculo():
    while True:
        archivo = open("vehiculo.txt",mode = "r+", encoding= "utf-8")
        tipoVehiculo = input(str("Ingrese el tipo de vehÍculo:"))
        cantPasajeros =input (str("Ingrese la cantidad de pasajeros del vehículo:"))
        cantEjes = input(str("Ingrese la cantidad de ejes del vehículo:"))
        infoVehiculo = [" TIPO DE VEHICULO: " + tipoVehiculo," CANTIDAD DE PASAJEROS:  " + cantPasajeros,   "CANTIDAD DE EJES: " + cantEjes]
        archivo.writelines(infoVehiculo)
        guardarVehiculo()
        archivo.close()
        print("¡El Vehículo ha sido guardado exitosamente!")

def agregarRepuesto():
    archivo = open("repuestos.txt", encoding= "utf-8", mode= "r+")
    nombre = input(str("Ingrese el nombre del repuesto:"))
    costoCompra = input(str ("Ingrese el costo del repuesto:"))
    precioVenta =input(str("Ingrese el precio de venta para el repuesto:"))
    infoRepuesto = [nombre, costoCompra, precioVenta]
    archivo.writelines(infoRepuesto)
    guardarRepuesto()
    archivo.close()
    print("¡El repuesto ha sido guardado exitosamente!")

def agregarManoObra():
    archivo = open("manoDeObra.txt", mode= "r+", encoding= "utf-8")
    nombreM = input(str("Ingrese el nombre del mecánico a cargo del vehículo:"))
    tiempo = input(int("Ingrese el tiempo estimado de ejecución:"))
    precio = input(int("Ingrese el precio final de mano de obra:"))
    infoManoObra = [nombreM, tiempo, precio]
    archivo.writelines(infoManoObra)
    guardarManoObra()
    archivo.close()

def agregarMantenimiento():
    archivo = open( "mantenimiento.txt", encoding= "utf-8", mode= "r+") 
    nombreMantenimiento = input(str("Ingrese el tipo de mantenimiento que desea realizar:"))
    tipoVehiculo = input("Elija el tipo de vehiculo", vehiculo)
    precioServicio = input("agregue el precio del servicio a cobrar:")
    infoMantenimiento = [nombreMantenimiento,tipoVehiculo,precioServicio] 
    archivo.writelines(infoMantenimiento)
    guardarMantenimiento()
    archivo.close()

#FUNCIÓN GUARDAR(Guarda las gestiones agregadas.)
def guardarVehiculo():
    guardarDato("vehiculo",vehiculo)

def guardarRepuesto():
    guardarDato("repuestos",repuestos)

def guardarManoObra():
    guardarDato("manoDeObra",mano_obra)
    
def guardarMantenimiento():
    guardarDato("mantenimiento",mantenimiento)

#FUNCIÓN MOSTRAR(Muestra las gestiones que han sido guardadas.)
def mostrarVehiculo():
    tablaMostrar(vehiculo)

def mostrarRepuesto():
    tablaMostrar(repuestos)

def mostrarManoObra():
    tablaMostrar(mano_obra)

def mostrarMantenimiento():
    tablaMostrar(mantenimiento)

#FUNCIÓN MODIFICAR


    
#def modVehiculo():

#def modRepuesto():

#def modManoObra():

#def modMantenimento():

#def reparaciones():

#def facturar():

#FUNCIONES DE CONSULTA
#def planesM():

#def genReservacion():

#def cancelReservacion():

#def consulReparacion():

#def consulFacturacion():

