"""
Módulo del menú principal
Maneja toda la interfaz de usuario de la máquina expendedora
"""

from maquina_expendedora import MaquinaExpendedora
from utilidades import *

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
            maquina.selecionar_producto(codigo) 
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
    pass

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

def ejecutar_maquina_expendedora():
    """
    Función principal que ejecuta la máquina expendedora
    """
    # TODO: Crear una instancia de MaquinaExpendedora
    # TODO: Cargar los productos iniciales
    # TODO: Mostrar el título
    # TODO: Crear un bucle principal que:
    #       - Limpie la pantalla
    #       - Muestre el menú principal
    #       - Pida al usuario que seleccione una opción
    #       - Procese la opción
    #       - Pause antes de continuar (excepto al salir)
    # TODO: El bucle debe continuar hasta que el usuario elija salir
    # 
    # Ejemplo de implementación:
    # maquina = MaquinaExpendedora()
    # maquina.cargar_productos_iniciales()
    # 
    # mostrar_titulo()
    # 
    # continuar = True
    # while continuar:
    #     mostrar_menu_principal()
    #     opcion = input("Selecciona una opción: ")
    #     
    #     continuar = procesar_opcion_menu(opcion, maquina)
    #     
    #     if continuar:
    #         pausar()
    #         limpiar_pantalla()
    # 
    # El bucle while se ejecuta hasta que continuar sea False
    # Esto pasa cuando el usuario elige la opción 7 (salir)
    pass

if __name__ == "__main__":
    # TODO: Llamar a la función ejecutar_maquina_expendedora()
    # 
    # Ejemplo de implementación:
    # ejecutar_maquina_expendedora()
    # 
    # Esta línea hace que el programa se ejecute cuando corras este archivo
    pass