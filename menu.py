"""
Módulo del menú principal
Maneja toda la interfaz de usuario de la máquina expendedora
"""

from utilidades import validar_numero_positivo, validar_codigo_producto
from maquina_expendedora import MaquinaExpendedora

def mostrar_menu_principal():
#Funcion que unicamente muestra un menu al usuario
    print("\n=== MENÚ PRINCIPAL ===")
    print("1- Ver productos disponibles")
    print("2- Insertar dinero ")
    print("3- Ver dinero insertado")
    print("4- Devolver dinero")
    print("5- Salir ")
    print("==========================================")
    pass

def procesar_opcion_menu(opcion, maquina):
  
    # TODO: Usar if/elif para manejar cada opción:
    
    # Opción 1: Mostrar productos disponibles
    # TODO: Llamar al método correspondiente de la máquina
    if opcion == 1:
        maquina.mostrar_productos_disponibles() #El orden para llamar la funcion correspondiente es primero la clase maquina y luego el nombre de la funcion
 
        
    
    # Opción 2: Insertar dinero
    # TODO: Pedir al usuario que ingrese la cantidad de dinero
    # TODO: Validar que sea un número positivo usando las utilidades
    # TODO: Llamar al método insertar_dinero de la máquina
    elif opcion == 2:
        cantidad_str = input("ingresa la cantidad de dinero que desees: $")
        es_valido, cantidad = validar_numero_positivo(cantidad_str) #aqui estamos usando una tupla (usamos dos variables para recibir los retornnos de la funcion en este caso true/false y un numero) Tambien le pasamos el valor a la funcion para que use el dato ingresado
        if es_valido: #Aqui preguntamos si regreso true/false segun si pasa la validacion (recordando que la variable es_valido tiene el valor de true o false)
            maquina.insertar_dinero(cantidad) #LLamamos a la funcion y le pasamos el dato de cantidad ingresada

    # Opción 3: Comprar producto
    # TODO: Pedir al usuario que ingrese el código del producto
    # TODO: Validar el código usando las utilidades
    # TODO: Llamar al método seleccionar_producto de la máquina
    
    elif opcion == 3:
        codigo = input("Ingresa el codigo del producto que deseas: ")
        if validar_codigo_producto(codigo):# llamamos a la funcion de utilidades que valida que el codigo tenga una letra y un numero en el orde 1A (la funcion devuelve un true/false)
            maquina.seleccionar_producto(codigo) 
        else:
            print("El codigo ingresado es invalido ")
    
    # Opción 4: Ver dinero insertado
    # TODO: Llamar al método correspondiente de la máquina
    elif opcion == 4:
        maquina.mostrar_dinero_insertado() #Unicamente muestra cuanto dinero ya se inserto(es para recordar al usuario que cantidad tiene)
        
    # Opción 5: Devolver dinero
    # TODO: Llamar al método devolver_dinero de la máquina
    elif opcion == 5:
        maquina.devolver_dinero() #Devuelve todo el dinero ingresado del usuario simplemente retorna una variable de acumulacion 
    
    # Opción : Modo administrador
    # TODO: Llamar al método modo_administrador de la máquina
    
    # Opción 6: Salir
    # TODO: Mostrar mensaje de despedida y retornar False
    elif opcion == 6:
        print("Vuelve pronto :) ")
        return False #este false apaga el bucle y sale del programa
    else:
        print("Opcion invalida")
    return True  # Agregar esta línea

#           Codigo Descartado
############################################################################################
def mostrar_menu_administrador():
    """
    Muestra las opciones del menú de administrador
    """
    # TODO: Mostrar un menú con opciones como:
    # 1. Ver inventario completo
    # 2. Reponer stock
    # 3. Agregar producto nuevo
    # 4. Volver al menú principal
    pass

def procesar_opcion_administrador(opcion, maquina):
    """
    Procesa las opciones del menú de administrador
    
    Args:
        opcion (str): Opción seleccionada
        maquina (MaquinaExpendedora): Instancia de la máquina
        
    Returns:
        bool: True para continuar en modo admin, False para volver al menú principal
    """
    # TODO: Implementar la lógica para cada opción del administrador
    # TODO: Similar a procesar_opcion_menu pero para las funciones de administrador
    pass
###############################################################################################



