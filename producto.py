"""
Módulo para la clase Producto
Representa un producto individual de la máquina expendedora
"""

class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        """
        Inicializa un producto
        
        Args:
            codigo (str): Código único del producto (ej: "A1", "B2")
            nombre (str): Nombre del producto (ej: "Coca Cola", "Papas")
            precio (float): Precio del producto
            cantidad (int): Cantidad disponible en stock
        """
        # TODO: Asignar los parámetros a los atributos de la clase
        # Ejemplo:
        # self.codigo = codigo
        # self.nombre = nombre
        # self.precio = precio
        # self.cantidad = cantidad
        pass
    
    def tiene_stock(self):
        """
        Verifica si el producto tiene stock disponible
        
        Returns:
            bool: True si hay stock (cantidad > 0), False caso contrario
        """
        # TODO: Implementar la lógica para verificar si hay stock
        # Ejemplo:
        # return self.cantidad > 0
        # 
        # Si self.cantidad es 5, retorna True
        # Si self.cantidad es 0, retorna False
        pass
    
    def comprar(self):
        """
        Realiza la compra del producto (reduce el stock en 1)
        
        Returns:
            bool: True si la compra fue exitosa, False si no hay stock
        """
        # TODO: Verificar si hay stock y reducir la cantidad en 1
        # TODO: Retornar True si se pudo comprar, False caso contrario
        # Ejemplo:
        # if self.cantidad > 0:
        #     self.cantidad = self.cantidad - 1  # También puedes usar: self.cantidad -= 1
        #     return True
        # else:
        #     return False
        #
        # Si había 5 productos, después de comprar quedarán 4
        pass
    
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
    
    def __str__(self):
        """
        Representación en string del producto para mostrar en pantalla
        
        Returns:
            str: Información formateada del producto
        """
        # TODO: Retornar una cadena con formato:
        # "[CODIGO] NOMBRE - $PRECIO (Stock: CANTIDAD)"
        # Ejemplo: "[A1] Coca Cola - $1.50 (Stock: 10)"
        # 
        # Ejemplo de implementación:
        # return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f} (Stock: {self.cantidad})"
        # 
        # El :.2f hace que el precio siempre muestre 2 decimales (ej: 1.50 en vez de 1.5)
        pass