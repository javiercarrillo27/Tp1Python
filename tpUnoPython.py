"""TP 1 Progrma para administrar una tienda de comercio electrónico"""

"""Punto 1 y 2 Gestionar Clientes y Productos"""
#Funciones




def cargarCliente(diccionarioCliente):                          #Creo un diccionario para el ingreso de los datos del cliente, y luego guardo sus valores en otro diccionario dentro del mismo.
    dni = input("Introduzca Dni del cliente: ")
    nombre = input("Introduzca Nombre del cliente: ")
    direccion = input("Introduzca Direccion del cliente: ")
    telefono = input("Introduzca Telefono del cliente: ")
    correo = input("Introduzca Correo del cliente: ")
    datos = {"nombre":nombre, "direccion":direccion, "telefono":telefono, "correo":correo}
    diccionarioCliente[dni]= datos                            #Creo el diccionario con los datos del cliente, la llave va a ser el DNI y el valor los datos 
    


def eliminarCampo(campo, diccionarioCliente):       #Funcion con Diccionario para eliminar cliente o productos, realizo la búsqueda y  recorro la lista.
    for i in list(diccionarioCliente):
        if i == campo:
            diccionarioCliente.pop(i)               #con pop elimino y retorno un elemento de la lista.
            print("El cliente DNI: ", campo,"ha sido eliminado con éxito.")
        else:
            if i != campo:
                print("Los datos ingresados son incorrectos, inténtelo nuevamente.")
            
            


def mostrarDato(campo, diccionario):                #Esta funcion con diccionario es utilizado para mostrar datos de clientes y productos en específico
    for i in list(diccionario):
        if i == campo:
            print("Los datos son: ", diccionario[i]) #si coincide la busqueda, muestra los datos
            


def mostrarTodosLosDatos(diccionario):                          #Funcion con Diccionario que muestra Todos los datos del/los clientes o productos existentes
    for i in list(diccionario):
        print("DNI / ID:" + str(i) + " " + str(diccionario[i]))
        



def nuevoProducto(producto):                                                #Creo un diccionario para cargar productos, el cual va a contener dentro otro diccionario con los productos ingresados
    numeroDeSerie = input("Introduzca Numero De Serie del producto: ")
    nombre = input("Introduzca Nombre del producto: ")
    tipo = input("Introduzca Tipo de producto: ")
    precioCosto = int(input("Introduzca Precio de Costo del producto: "))
    precioVenta = int(input("Introduzca Precio de Venta del producto: "))
    stock = int(input("Introduzca Stock del producto: "))
    datos = {"nombre":nombre, "tipo":tipo, "precioCosto":precioCosto, "precioVenta":precioVenta, "stock":stock}  #Estos datos son cargados a este diccionario
    producto[numeroDeSerie]= datos
    

def venta (dni, numeroDeSerie, productos, totalVentasMensual, meses):
    while True:
        i = 0                                                               #Inicio la iteracion de los meses en Cero
        mes = input("Ingrese mes de la venta: ")
        for i in range(len (meses)):                                        #Itero por los meses
            if mes == meses[i]:                                             #Si el mes existe continúa
                cantidad = int(input("Ingrese la cantidad de productos que desea vender: "))              #Ingresamos la cantidad de productos
                precio = 0                                                  #Inicio la variable del precio en Cero
                producto = productos[numeroDeSerie]                         #Obtenemos el diccionario solo
                stock = producto.get("stock")                               #Stock del producto que deseo vencer
                precioVenta = producto.get("precioVenta")
                if stock != 0 and stock >= cantidad:                        #Comprobamos que hay stock, si ha stock continúa
                    precio = precioVenta                                    #Colocamos el precio de venta
                    precio = precio * cantidad                              #Calculamos el total
                                                                            
                    ventasMensuales(precio, mes, totalVentasMensual, meses) #Se carga la venta en el mes que corresponde en la lista de ventas mensuales
                    return (mes, numeroDeSerie, precio, dni)                #Retorno la tupla
                else:
                    print("No hay stock")                   
                venta(dni, numeroDeSerie, productos, totalVentasMensual, meses)
        print("Ingreso incorrecto del mes.")                            
    
    
    
def ventasMensuales(precio, mes, totalVentasMensual, meses):            #Funcion para guardar las ventas mensuales
    i = 0                                                               #El indice que recorre la lista
    for i in range(len(meses)):                                         #Recorremos la lista
        if mes == meses[i]:                                             #Si el mes es igual al mes, continua
            totalVentasMensual[i] = totalVentasMensual[i] + precio      #Actualizamos el valor
    return


def buscarProducto(productos, numeroDeSerie):        #Busco un producto por su numero de serie
    for p in productos.items():                      #Paso la lista de productos y el numero de serie
        if p == numeroDeSerie:                       
            return p
        

def listar_productos(productos):            #funcion para listar productos
    for p in productos.items():             #itero por cada producto que existe en la lista de productos
        print(p["numeroDeSerie"])           #el usuario ingresa el id del producto que desea vender y me traigo el nombre y el id
    
    


def mostrarVentasMensuales(totalVentasMensual, meses, i):       #funcion para mostrar el total de ventas mensuales de cada mes... Itero por la lista de meses y totalVentasMensual
    if i < (len(meses)-1):
        print(meses[i], ": ", totalVentasMensual[i])
        mostrarVentasMensuales(totalVentasMensual, meses, i+1)
    if i == (len(meses)-1):
        print(meses[i], ": " , totalVentasMensual[i])
        
       
def obtenerTotales(total, totalVentasMensual):                 #Funcion que recibe el total a comparar ingresado por el usuario y la lista con todas las ventas registradas por mes:
    totalesMensuales = []
    i = 0
    for i in range(len(totalVentasMensual)):                    #Itero por las ventas mensuales
        if totalVentasMensual[i] > total:
            totalesMensuales.append(totalVentasMensual[i])      #Si el valor es mayor al total a comparar, se agrega a la lista
    return totalesMensuales                                     # Retorna los nuevos valores mensuales
        
def sumarPorcentaje(totalVentasMensual):                        #Funcion que toma las ventas mensuales y les agrega un 25%
    i = 0
    for i in range(len(totalVentasMensual)):                    #Itero por las ventas mesuales
        totalVentasMensual[i] = totalVentasMensual[i] + ((totalVentasMensual[i] * 25) / 100)        #Agrego el 25% a la venta
        print (totalVentasMensual)
    return totalVentasMensual                                                                         #Retorno el nuevo valor mensual


# Lista de meses
meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

#Lista de total ventas mensuales
totalVentasMensual = [0,1,2,3,4,5,6,7,8,9,10,11]

#Lista ventasMensuales
totalesMensuales = []

#Lista ventas mensuales + 25%

totalMensualConPorcentaje = []

#diccionario de productos
productos = {}

#diccionario de clientes
diccionarioCliente = {}

#Programa

opcion = ''

while opcion != "13":                                                   #Ingreso al programa al menos una vez
    
    if opcion == '1':                                                   #Cargar nuevo cliente
        cargarCliente(diccionarioCliente)
        
    if opcion =="2":                                                    #Eliminar cliente por DNI
        dni = input("Ingrese DNI del cliente: ")
        eliminarCampo(dni, diccionarioCliente)
    
    if opcion =="3":                                                    #Buscar cliente por DNI
        dni = input("Introduzca el Dni del cliente que desea buscar: ")
        mostrarDato(dni, diccionarioCliente)
            
    if opcion == "4":                                                   #Listar todos los clientes
        print ("Lista de clientes: ")
        mostrarTodosLosDatos(diccionarioCliente)
        
        
    if opcion == '5':                                                   #Cargar nuevo producto
        nuevoProducto(productos)
        
    if opcion =="6":                                                    #Eliminar producto
        numeroDeSerie = input("Ingrese número de serie del producto: ")
        eliminarCampo(numeroDeSerie, productos)
    
    if opcion =="7":                                                    #Buscar producto
        numeroDeSerie = input("Introduzca el número de serie del producto que desea buscar: ")
        mostrarDato(numeroDeSerie, productos)
            
    if opcion == "8":                                                   #Listar todos los productos
        print ("Lista de Productos: ")
        mostrarTodosLosDatos(productos)
    
    if opcion == '9':#Registrar venta
        while True:
            numeroDeSerie = input("Ingrese el número de serie del producto que desea vender: ")
            dni = input("Ingrese el DNI del cliente: ")
            venta(dni, numeroDeSerie, productos, totalVentasMensual, meses)
            print("La venta se realizó con éxito.")
            break
        
    if opcion == '10':                                          #Imprimo el total las ventas mensuales de cada mes del año
        mostrarVentasMensuales(totalVentasMensual, meses, 0)
        
    
    if opcion == "11":                                          #Muestro una lista con los totales de cada mes que son mayores al número ingresado por el usuario
                while True:
                    totalOrdenesMensuales = []
                    total = int(input("Ingrese el valor del total de ventas que desea mostrar: "))
                    totalOrdenesMensuales = obtenerTotales(total, totalVentasMensual)
                    print(totalOrdenesMensuales)
                    break
                
    if opcion == "12":                                           #Sumo un 25%  a las ventas mensuales
        sumarPorcentaje(totalVentasMensual)

    if opcion == "13":
        break    

    opcion = input("Elija una opción del menú que desea ejecutar:\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar datos de cliente\n(4) Listar todos los clientes\n(5) Cargar producto\n(6) Eliminar producto\n(7) Mostrar producto\n(8) Mostrar todos los productos\n(9) Registrar venta\n(10) Total de ventas por mes\n(11) Total de cada mes\n(12) Total de ventas mensual con 25% más\n(13) Terminar\n Elige una opción: ")
        
        












"""   
cliente = {}
opcion = ''

while opcion != "5":
    if opcion == '1':
        dni = input("Introduzca Dni del cliente: ")
        nombre = input("Introduzca Nombre del cliente: ")
        direccion = input("Introduzca Direccion del cliente: ")
        telefono = input("Introduzca Telefono del cliente: ")
        correo = input("Introduzca Correo del cliente: ")
        datos = {"nombre":nombre, "direccion":direccion, "telefono":telefono, "correo":correo}
        cliente[dni]= datos
        
    if opcion =="2":
        dni = input("Ingrese DNI del cliente: ")
        if dni in cliente:
            del cliente[dni]
        else:
            print("No existe ningún cliente con el DNI ",dni)
    
    if opcion =="3":
        dni = input("Introduzca el Dni del cliente que desea buscar: ")
        if dni in cliente:
            print ("Dni: ",dni)
            for clave,valor in cliente[dni].items():
                print(clave.title() + ":", valor)
        else:
            print("No existe ningún cliente con el DNI ",dni)
            
    if opcion == "4":
        print ("Lista de clientes: ")
        for clave, valor in cliente.items():
            print(clave, valor["nombre"])
        
    opcion = input("Elija una opción del menú que desea ejecutar\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Terminar\n Elige una opción: ")"""
        
        
"""Punto 2 Gestionar Productos"""
"""

producto = {}
opcion = ''

while opcion != "5":
    if opcion == '1':
        numeroDeSerie = input("Introduzca Numero De Serie del producto: ")
        nombre = input("Introduzca Nombre del producto: ")
        tipo = input("Introduzca Tipo de producto: ")
        precioCosto = input("Introduzca Precio de Costo del producto: ")
        precioVenta = input("Introduzca Precio de Venta del producto: ")
        stock = input("Introduzca Stock del producto: ")
        datos = {"nombre":nombre, "tipo":tipo, "precioCosto":precioCosto, "precioVenta":precioVenta, "stock":stock}
        producto[numeroDeSerie]= datos
        
    if opcion =="2":
        numeroDeSerie = input("Ingrese Numero de Serie del producto: ")
        if numeroDeSerie in producto:
            del producto[numeroDeSerie]
        else:
            print("No existe ningún producto con el número de serie: ",numeroDeSerie)
    
    if opcion =="3":
        numeroDeSerie = input("Introduzca el Número de Serie del producto que desea buscar: ")
        if numeroDeSerie in producto:
            print ("numeroDeSerie: ",numeroDeSerie)
            for clave,valor in producto[numeroDeSerie].items():
                print(clave.title() + ":", valor)
        else:
            print("No existe ningún producto con el número de serie: ",numeroDeSerie)
            
    if opcion == "4":
        print ("Lista de productos: ")
        for clave, valor in producto.items():
            print(clave, valor["nombre"])
        
    opcion = input("Elija una opción del menú que desea ejecutar\n(1) Añadir producto\n(2) Eliminar producuto\n(3) Mostrar producto\n(4) Listar productos\n(5) Terminar\n Elige una opción: ")"""
        
        
"""Punto 3 Gestionar Ventas Realizadas

mesVenta = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
numeroDeSerie = []
precioTotal = []
dniCliente = []
"""




