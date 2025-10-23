"""
Módulo del menú principal
Maneja toda la interfaz de usuario de la máquina expendedora
"""

from maquina_expendedora import MaquinaExpendedora
from utilidades import *

def mostrar_menu_principal():
    """
    Muestra las opciones del menú principal
    """
    # TODO: Mostrar un menú atractivo con las siguientes opciones:
    # 1. Ver productos disponibles
    # 2. Insertar dinero
    # 3. Comprar producto
    # 4. Ver dinero insertado
    # 5. Devolver dinero
    # 6. Modo administrador
    # 7. Salir
    # 
    # Ejemplo de implementación:
    # print("\n=== MENÚ PRINCIPAL ===")
    # print("1. Ver productos disponibles")
    # print("2. Insertar dinero")
    # print("3. Comprar producto")
    # print("4. Ver dinero insertado")
    # print("5. Devolver dinero")
    # print("6. Modo administrador")
    # print("7. Salir")
    # print("=" * 22)
    pass

def procesar_opcion_menu(opcion, maquina):
    """
    Procesa la opción seleccionada del menú principal
    
    Args:
        opcion (str): Opción seleccionada por el usuario
        maquina (MaquinaExpendedora): Instancia de la máquina expendedora
        
    Returns:
        bool: True para continuar el programa, False para salir
    """
    # TODO: Usar if/elif para manejar cada opción:
    
    # Opción 1: Mostrar productos disponibles
    # TODO: Llamar al método correspondiente de la máquina
    
    # Opción 2: Insertar dinero
    # TODO: Pedir al usuario que ingrese la cantidad de dinero
    # TODO: Validar que sea un número positivo usando las utilidades
    # TODO: Llamar al método insertar_dinero de la máquina
    
    # Opción 3: Comprar producto
    # TODO: Pedir al usuario que ingrese el código del producto
    # TODO: Validar el código usando las utilidades
    # TODO: Llamar al método seleccionar_producto de la máquina
    
    # Opción 4: Ver dinero insertado
    # TODO: Llamar al método correspondiente de la máquina
    
    # Opción 5: Devolver dinero
    # TODO: Llamar al método devolver_dinero de la máquina
    
    # Opción 6: Modo administrador
    # TODO: Llamar al método modo_administrador de la máquina
    
    # Opción 7: Salir
    # TODO: Mostrar mensaje de despedida y retornar False
    
    # Opción inválida
    # TODO: Mostrar mensaje de error
    
    # TODO: Retornar True para todas las opciones excepto salir
    # 
    # Ejemplo de implementación básica:
    # if opcion == "1":
    #     maquina.mostrar_productos_disponibles()
    # elif opcion == "2":
    #     cantidad_str = input("Ingresa la cantidad de dinero: $")
    #     es_valido, cantidad = validar_numero_positivo(cantidad_str)
    #     if es_valido:
    #         maquina.insertar_dinero(cantidad)
    #     else:
    #         print("Cantidad inválida.")
    # elif opcion == "3":
    #     codigo = input("Ingresa el código del producto: ")
    #     if validar_codigo_producto(codigo):
    #         maquina.seleccionar_producto(codigo)
    #     else:
    #         print("Código inválido.")
    # elif opcion == "4":
    #     maquina.mostrar_dinero_insertado()
    # elif opcion == "5":
    #     maquina.devolver_dinero()
    # elif opcion == "7":
    #     print("¡Gracias por usar la máquina expendedora!")
    #     return False
    # else:
    #     print("Opción inválida.")
    # return True
    pass

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