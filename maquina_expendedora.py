
#Módulo para la clase MaquinaExpendedora
#Maneja toda la lógica de la máquina expendedora
###########################################################################################################


from producto import Producto # esto importa producto desde otro archivo llamado producto.py

class MaquinaExpendedora:
    def __init__(self):

    #class(clase): podra guardar productos, recibir cambio y vender productos( mas adelante)
    #init: es el constructor de la clase, su funcion es inicializar los atrubutos(variables internas) 

 #Inicializa la máquina expendedora
    
        self.productos ={} #diccionario vacio llamado productos (guarda todos los productos disponibles)
        self.dinero_insertado = 0.0  #comienza desde cero por que nadie ha ingresado nada aun

##########################################################################################################   
    def cargar_productos_iniciales(self):
        """
        Carga los productos iniciales de la máquina
        Puedes modificar esta función para agregar los productos que desees
        """
        # TODO: Crear varios productos usando la clase Producto
        # Ejemplos sugeridos:
        # - A1: Coca Cola, $1.50, 10 unidades
        # - A2: Pepsi, $1.50, 8 unidades
        # - B1: Papas Lays, $2.00, 15 unidades
        # - B2: Doritos, $2.25, 12 unidades
        # - C1: Chocolate Kit Kat, $1.75, 6 unidades
        # - C2: Chicles Trident, $0.75, 20 unidades
        
        # TODO: Agregar cada producto al diccionario usando su código como clave
        # 
        # Ejemplo de implementación:
        # coca = Producto("A1", "Coca Cola", 1.50, 10)
        # pepsi = Producto("A2", "Pepsi", 1.50, 8)
        # papas = Producto("B1", "Papas Lays", 2.00, 15)
        # 
        # self.productos["A1"] = coca
        # self.productos["A2"] = pepsi  
        # self.productos["B1"] = papas
        # 
        # Otra forma más corta:
        # self.productos["A1"] = Producto("A1", "Coca Cola", 1.50, 10)
        # self.productos["A2"] = Producto("A2", "Pepsi", 1.50, 8)
        pass
    
    def mostrar_productos_disponibles(self):
        """
        Muestra todos los productos disponibles en la máquina
        """
        # TODO: Imprimir un encabezado atractivo
        # TODO: Iterar sobre todos los productos y mostrar solo los que tienen stock
        # TODO: Si no hay productos disponibles, mostrar un mensaje apropiado
        # 
        # Ejemplo de implementación:
        # print("=== PRODUCTOS DISPONIBLES ===")
        # productos_disponibles = 0
        # 
        # for codigo, producto in self.productos.items():
        #     if producto.tiene_stock():
        #         print(producto)  # Esto llama al método __str__ del producto
        #         productos_disponibles += 1
        # 
        # if productos_disponibles == 0:
        #     print("No hay productos disponibles en este momento.")
        # 
        # El bucle for recorre el diccionario:
        # - codigo será "A1", "A2", etc.
        # - producto será el objeto Producto correspondiente
        pass
    
    def insertar_dinero(self, cantidad):
        """
        Permite al usuario insertar dinero en la máquina
        
        Args:
            cantidad (float): Cantidad de dinero a insertar
            
        Returns:
            bool: True si el dinero se insertó correctamente, False caso contrario
        """
        # TODO: Validar que la cantidad sea positiva
        # TODO: Agregar la cantidad al dinero total insertado
        # TODO: Mostrar mensaje de confirmación
        # TODO: Retornar True si fue exitoso, False caso contrario
        # 
        # Ejemplo de implementación:
        # if cantidad > 0:
        #     self.dinero_insertado += cantidad
        #     print(f"Has insertado ${cantidad:.2f}")
        #     print(f"Total insertado: ${self.dinero_insertado:.2f}")
        #     return True
        # else:
        #     print("La cantidad debe ser mayor que cero.")
        #     return False
        # 
        # Si insertas $2.00 y ya tenías $1.50, el total será $3.50
        pass
    
    def mostrar_dinero_insertado(self):
        """
        Muestra la cantidad de dinero insertado actualmente
        """
        # TODO: Mostrar el dinero insertado con formato de moneda
        # 
        # Ejemplo de implementación:
        # print(f"Dinero insertado: ${self.dinero_insertado:.2f}")
        # 
        # Si has insertado $3.50, mostrará: "Dinero insertado: $3.50"
        pass
    
    def seleccionar_producto(self, codigo):
        """
        Permite al usuario seleccionar un producto para comprar
        
        Args:
            codigo (str): Código del producto seleccionado
            
        Returns:
            bool: True si la compra fue exitosa, False caso contrario
        """
        # TODO: Convertir el código a mayúsculas para evitar errores
        # TODO: Verificar si el producto existe en el diccionario
        # TODO: Verificar si el producto tiene stock
        # TODO: Verificar si el dinero insertado es suficiente para comprar el producto
        # TODO: Si todo está correcto:
        #       - Realizar la compra del producto
        #       - Calcular el cambio (dinero insertado - precio del producto)
        #       - Mostrar mensaje de compra exitosa con el producto y el cambio
        #       - Resetear el dinero insertado a 0
        #       - Retornar True
        # TODO: Si hay algún error, mostrar mensaje apropiado y retornar False
        # 
        # Ejemplo de implementación:
        # codigo = codigo.upper()  # Convierte "a1" en "A1"
        # 
        # if codigo not in self.productos:
        #     print("Producto no encontrado.")
        #     return False
        # 
        # producto = self.productos[codigo]
        # 
        # if not producto.tiene_stock():
        #     print("Producto agotado.")
        #     return False
        # 
        # if self.dinero_insertado < producto.precio:
        #     print(f"Dinero insuficiente. Necesitas ${producto.precio:.2f}")
        #     return False
        # 
        # # Todo está bien, realizar compra
        # if producto.comprar():
        #     cambio = self.dinero_insertado - producto.precio
        #     print(f"¡Compra exitosa! {producto.nombre}")
        #     print(f"Tu cambio: ${cambio:.2f}")
        #     self.dinero_insertado = 0
        #     return True
        pass
    
    def devolver_dinero(self):
        """
        Devuelve todo el dinero insertado al usuario
        
        Returns:
            float: Cantidad de dinero devuelto
        """
        # TODO: Guardar la cantidad de dinero a devolver
        # TODO: Mostrar mensaje de devolución
        # TODO: Resetear el dinero insertado a 0
        # TODO: Retornar la cantidad devuelta
        # 
        # Ejemplo de implementación:
        # dinero_devuelto = self.dinero_insertado
        # 
        # if dinero_devuelto > 0:
        #     print(f"Devolviendo ${dinero_devuelto:.2f}")
        #     self.dinero_insertado = 0
        # else:
        #     print("No hay dinero para devolver.")
        # 
        # return dinero_devuelto
        # 
        # Si tenías $5.00 insertados, devuelve $5.00 y queda en $0.00
        pass
    
    def modo_administrador(self):
        """
        Modo especial para administrar la máquina (reponer stock, ver inventario completo)
        """
        # TODO: Implementar un menú para el administrador con opciones como:
        # - Ver inventario completo (incluye productos sin stock)
        # - Reponer stock de un producto específico
        # - Agregar nuevo producto
        # - Volver al modo usuario
        # 
        # Ejemplo de implementación:
        # print("=== MODO ADMINISTRADOR ===")
        # print("1. Ver inventario completo")
        # print("2. Reponer stock")
        # print("3. Volver al menú principal")
        # 
        # opcion = input("Selecciona una opción: ")
        # 
        # if opcion == "1":
        #     self.mostrar_inventario_completo()
        # elif opcion == "2":
        #     codigo = input("Código del producto: ")
        #     cantidad_str = input("Cantidad a reponer: ")
        #     # Aquí usarías validaciones y llamarías a reponer_stock_producto
        # elif opcion == "3":
        #     print("Volviendo al menú principal...")
        pass
    
    def mostrar_inventario_completo(self):
        """
        Muestra todos los productos, incluso los que no tienen stock
        Solo para uso del administrador
        """
        # TODO: Mostrar todos los productos del diccionario
        # TODO: Indicar claramente cuáles no tienen stock
        # 
        # Ejemplo de implementación:
        # print("=== INVENTARIO COMPLETO ===")
        # 
        # for codigo, producto in self.productos.items():
        #     estado = "DISPONIBLE" if producto.tiene_stock() else "SIN STOCK"
        #     print(f"{producto} - {estado}")
        # 
        # if len(self.productos) == 0:
        #     print("No hay productos en el inventario.")
        # 
        # Este método muestra TODOS los productos, no solo los disponibles
        pass
    
    def reponer_stock_producto(self, codigo, cantidad):
        """
        Repone el stock de un producto específico
        
        Args:
            codigo (str): Código del producto
            cantidad (int): Cantidad a reponer
            
        Returns:
            bool: True si se repuso correctamente, False caso contrario
        """
        # TODO: Verificar que el producto exista
        # TODO: Validar que la cantidad sea positiva
        # TODO: Reponer el stock usando el método del producto
        # TODO: Mostrar mensaje de confirmación
        # TODO: Retornar True si fue exitoso, False caso contrario
        # 
        # Ejemplo de implementación:
        # codigo = codigo.upper()
        # 
        # if codigo not in self.productos:
        #     print("Producto no encontrado.")
        #     return False
        # 
        # if cantidad <= 0:
        #     print("La cantidad debe ser mayor que cero.")
        #     return False
        # 
        # producto = self.productos[codigo]
        # producto.reponer_stock(cantidad)
        # print(f"Stock repuesto: {cantidad} unidades de {producto.nombre}")
        # print(f"Stock actual: {producto.cantidad}")
        # return True
        pass