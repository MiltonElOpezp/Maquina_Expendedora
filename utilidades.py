
#Módulo de utilidades para validación y formato
#Funciones auxiliares para la máquina expendedora
##################################################################################################
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

 #Formatea un precio con el objetivo de mostrarlo con el símbolo de moneda y dos decimales
    
    return f"${precio:.2f}"
  
    # f-strings: para formatear el número 
    # :.2f : para asegurar que siempre muestre 2 decimales

    # Ejemplos de uso:
    # formatear_precio(1.5) → "$1.50"
    # formatear_precio(2.0) → "$2.00" 
    # formatear_precio(0.75) → "$0.75"

###########################################################################################################
def limpiar_pantalla():
    
    #Limpia la pantalla de la consola como si fuera una nueva 
    
    # OS: para ejecutar comandos del sistema
    # cls: comando para limpiar pantalla en Windows
    # clear: comando para limpiar pantalla en Linux/Mac

    import os
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Mac
        os.system('clear')

 #Esta función borra todo lo que hay en la consola, como si empezaras de nuevo.
 #Esto es util  para que la pantalla no se llene de texto y sea más fácil de leer antes de mostar un nuevo menu o mensaje.

###########################################################################################################    
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