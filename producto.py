"""
Módulo para la clase Producto
Representa un producto individual de la máquina expendedora
"""

class Producto: #Esta clase sirve para crear los productos que van a estar en la maquina expendedora
    def __init__(self, codigo, nombre, precio, cantidad): #Esta es una funcion que le da parametros a cada producto es decir lo que debe de tener cada producto
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad 
        #Self sirve para referirse a la misma clase o al mismo objeto en el lenguaje de c# se usa this. 

    
    def tiene_stock(self): 
      
        return self.cantidad > 0 #Esto sirve para verificar si aun hay stock de los productos
        #Si el producto si existe devuelde un verdadero o de caso contrario devuelve un falso (esto sirve para la toma de deciciones)
    
    def comprar(self):
        if self.cantidad > 0: #Si la cantidad es mayor a 0
            self.cantidad -= 1 #Se le resta uno a la cantidad
            return True #Devuelve un verdadero
        else:
            return False #Devuelve un falso ya que no hay stock disponible
            #Codigo Descartado
    ##################################################################
    def reponer_stock(self, cantidad):
        """
        Repone el stock del producto
        
        Args:
            cantidad (int): Cantidad a agregar al stock actual
        """
        # TODO: Agregar la cantidad especificada al stock actual
        # Ejemplo:
        # self.cantidad = self.cantidad + cantidad  # También puedes usar: self.cantidad += cantidad
        #
        # Si tenías 3 productos y repones 10, quedarás con 13 productos
        pass
    #################################################################################
    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f} (Stock: {self.cantidad})" #Sirve para mostrar en pantalla los productos con su codigo, nombre, precio y cantidad
         # Ejemplo: "[A1] Coca Cola - $1.50 (Stock: 10)"
