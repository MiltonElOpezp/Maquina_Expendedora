
#Módulo de utilidades para validación y formato
#Funciones auxiliares para la máquina expendedora

def validar_numero_positivo(entrada):

 ## Valida que la entrada sea un número positivo y si no lo es, retorna False
    
    try:
        numero = float(entrada) # Convierte la entrada a float
        if numero > 0: # Verifica si el número es positivo, ejemplo: 1, 2.5, etc.
            return (True, numero) # True: indica que es válido, Numero: el valor numerico convertido
        else:
            return (False, None) # No es positivo, ejjemplo: 0, -3, etc.
    except ValueError:
        return (False, None) # No es un número válido o no hay numero, ejemplo: "abc", etc.
 
 # Ejemplos de uso:
 # validar_numero_positivo("2.50") → (True, 2.50)
 # validar_numero_positivo("-1") → (False, None) 
 # validar_numero_positivo("abc") → (False, None)

##########################################################################################################
def validar_codigo_producto(codigo):
    
 ##Valida que un código de producto tenga el formato correcto (una letra + un número)
    #letra:isalpha()
    #número:isdigit()

    if len(codigo) != 2: # Verifica que el código tenga exactamente 2 caracteres
        return False
    
    # Ejemplos:
    #"A1" → tiene 2 caracteres → sigue
    #"AB1" → tiene 3 caracteres → devuelve False
    #"A" → tiene 1 carácter → devuelve False

    letra = codigo[0]  # Primer carácter posición 0
    numero = codigo[1]  # Segundo carácter posición 1
    
    #Ejemplos:
    #codigo = "A1"
    #letra = "A"    
    #numero = "1"

    if letra.isalpha() and numero.isdigit(): # Verifica que el primer carácter sea una letra y el segundo un número
        return True # Formato correcto
    else:
        return False # Formato incorrecto
   
    # Ejemplos de uso:
    # validar_codigo_producto("A1") → True
    # validar_codigo_producto("B2") → True
    # validar_codigo_producto("1A") → False
    # validar_codigo_producto("AB") → False
    
############################################################################################################
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
###########################################################################################################
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