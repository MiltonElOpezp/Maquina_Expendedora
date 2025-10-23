"""
Módulo de utilidades para validación y formato
Funciones auxiliares para la máquina expendedora
"""

def validar_numero_positivo(entrada):
    """
    Valida que una entrada sea un número positivo
    
    Args:
        entrada (str): Entrada del usuario a validar
        
    Returns:
        tuple: (es_valido, numero) donde es_valido es bool y numero es float o None
    """
    # TODO: Intentar convertir la entrada a float
    # TODO: Verificar que el número sea positivo
    # TODO: Retornar (True, numero) si es válido, (False, None) si no es válido
    # TODO: Manejar excepciones si la conversión falla
    # 
    # Ejemplo de implementación:
    # try:
    #     numero = float(entrada)
    #     if numero > 0:
    #         return (True, numero)
    #     else:
    #         return (False, None)
    # except ValueError:
    #     return (False, None)
    # 
    # Ejemplos de uso:
    # validar_numero_positivo("2.50") → (True, 2.50)
    # validar_numero_positivo("-1") → (False, None) 
    # validar_numero_positivo("abc") → (False, None)
    pass

def validar_codigo_producto(codigo):
    """
    Valida que un código de producto tenga el formato correcto
    
    Args:
        codigo (str): Código a validar
        
    Returns:
        bool: True si el formato es válido, False caso contrario
    """
    # TODO: Verificar que el código no esté vacío
    # TODO: Verificar que tenga el formato correcto (una letra seguida de un número)
    # TODO: Ejemplos válidos: A1, B2, C3, etc.
    # TODO: Retornar True si es válido, False caso contrario
    # 
    # Ejemplo de implementación:
    # if len(codigo) != 2:
    #     return False
    # 
    # primera_letra = codigo[0]  # Primer carácter
    # segundo_numero = codigo[1]  # Segundo carácter
    # 
    # if primera_letra.isalpha() and segundo_numero.isdigit():
    #     return True
    # else:
    #     return False
    # 
    # Ejemplos de uso:
    # validar_codigo_producto("A1") → True
    # validar_codigo_producto("B2") → True
    # validar_codigo_producto("12") → False (no tiene letra)
    # validar_codigo_producto("AB") → False (no tiene número)
    pass

def formatear_precio(precio):
    """
    Formatea un precio para mostrar en pantalla
    
    Args:
        precio (float): Precio a formatear
        
    Returns:
        str: Precio formateado con símbolo de moneda
    """
    # TODO: Retornar el precio formateado como "$X.XX"
    # TODO: Asegurar que siempre muestre 2 decimales
    # 
    # Ejemplo de implementación:
    # return f"${precio:.2f}"
    # 
    # Ejemplos de uso:
    # formatear_precio(1.5) → "$1.50"
    # formatear_precio(2.0) → "$2.00" 
    # formatear_precio(0.75) → "$0.75"
    pass

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola
    """
    # TODO: Importar os
    # TODO: Usar os.system('cls') para Windows o os.system('clear') para Linux/Mac
    # TODO: Alternativamente, imprimir varias líneas vacías
    # 
    # Ejemplo de implementación:
    # import os
    # os.system('cls')  # Para Windows
    # 
    # O si quieres que funcione en cualquier sistema:
    # import os
    # if os.name == 'nt':  # Windows
    #     os.system('cls')
    # else:  # Linux/Mac
    #     os.system('clear')
    # 
    # Alternativa simple sin importar nada:
    # print("\n" * 50)  # Imprime 50 líneas vacías
    pass

def mostrar_titulo():
    """
    Muestra un título atractivo para la máquina expendedora
    """
    # TODO: Crear un título ASCII art o con caracteres especiales
    # TODO: Ejemplo:
    # ================================
    #     MÁQUINA EXPENDEDORA 3000
    # ================================
    # 
    # Ejemplo de implementación:
    # print("=" * 40)
    # print("     MÁQUINA EXPENDEDORA 3000")
    # print("=" * 40)
    # print()  # Línea vacía
    # 
    # O más elaborado:
    # print("╔" + "═" * 38 + "╗")
    # print("║        MÁQUINA EXPENDEDORA         ║")
    # print("║              3000                  ║")
    # print("╚" + "═" * 38 + "╝")
    pass

def pausar():
    """
    Pausa la ejecución hasta que el usuario presione Enter
    """
    # TODO: Usar input() con un mensaje como "Presiona Enter para continuar..."
    # 
    # Ejemplo de implementación:
    # input("Presiona Enter para continuar...")
    # 
    # O con más estilo:
    # input("\n--- Presiona Enter para continuar ---")
    pass