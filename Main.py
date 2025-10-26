"""
ARCHIVO PRINCIPAL - MÁQUINA EXPENDEDORA
=======================================

Este es el archivo principal para ejecutar la máquina expendedora.
Todo el código está dividido en módulos para mejor organización:

- producto.py: Clase Producto que representa cada item
- maquina_expendedora.py: Clase principal que maneja toda la lógica
- utilidades.py: Funciones auxiliares para validaciones y formato
- menu.py: Interfaz de usuario y menús

INSTRUCCIONES PARA IMPLEMENTAR:
==============================

1. Comienza implementando la clase Producto en producto.py
   - Son funciones simples de getters, setters y validaciones

2. Luego implementa las utilidades en utilidades.py
   - Funciones de validación y formato que usarás en otros módulos

3. Después implementa MaquinaExpendedora en maquina_expendedora.py
   - Esta es la lógica principal del programa

4. Finalmente implementa los menús en menu.py
   - La interfaz de usuario que conecta todo

5. Para ejecutar el programa, descomenta la línea al final de este archivo

CARACTERÍSTICAS A IMPLEMENTAR:
=============================
✓ Sistema de productos con código, nombre, precio y stock
✓ Inserción y manejo de dinero
✓ Compra de productos con validación de stock y dinero
✓ Sistema de cambio/vuelto
✓ Devolución de dinero
✓ Modo administrador para gestionar inventario
✓ Validaciones de entrada del usuario
✓ Interfaz clara y fácil de usar

¡Buena suerte programando! 🚀
"""

# Importar el módulo del menú principal
from maquina_expendedora import MaquinaExpendedora #Esto sirve para llamar a las funciones de diferentes archivos siemppre y cuando esten en la misma carpeta
from menu import mostrar_menu_principal, procesar_opcion_menu
from utilidades import limpiar_pantalla, pausar, mostar_titulo 


# TODO: Descomenta la siguiente línea cuando hayas implementado todas las funciones
# ejecutar_maquina_expendedora()
def ejecutar_maquina_expendedora():
    """
    Función principal que ejecuta la máquina expendedora
    """
    # TODO: Crear una instancia de MaquinaExpendedora
    maquina = MaquinaExpendedora()
    
    
    # TODO: Cargar los productos iniciales
    maquina.cargar_productos_iniciales()
    # TODO: Mostrar el título
    mostar_titulo()
    
    # TODO: Crear un bucle principal que:
    bandera = True
    while bandera:
        limpiar_pantalla()
        mostrar_menu_principal()
        try:
            opcion_str = input("Seleccione una opcion: ")
            opcion = int(opcion_str)
            bandera = procesar_opcion_menu(opcion, maquina)
        except ValueError:
            print("Por favor ingresa un número válido.")
            bandera = True
            if bandera:
               pausar()

if __name__ == "__main__":
   ejecutar_maquina_expendedora()


    
