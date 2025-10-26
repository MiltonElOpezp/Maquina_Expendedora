
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

        #Carga los productos iniciales de la máquina
        #Se puede modificar esta función para agregar los productos que se desee
        
        #LUGAR:A
        #FILAS:1 AL 5
        self.productos["A1"] = Producto("A1", "Base líquida", 300, 6)
        self.productos["A2"] = Producto("A2", "Base en crema", 350, 6)
        self.productos["A3"] = Producto("A3", "Polvo compacto", 200, 6)
        self.productos["A4"] = Producto("A4", "Polvo suelto", 250, 6)
        self.productos["A5"] = Producto("A5","Corrector", 150, 6)

        #LUGAR:B
        #FILAS:1 AL 5
        self.productos["B1"] = Producto("B1", "Iluminador", 200, 6)
        self.productos["B2"] = Producto("B2", "Colorete (blush)", 150,6)
        self.productos["B3"] =Producto("B3", "Bronceador", 200, 6)
        self.productos["B4"] = Producto("B4", "Sombra de ojos", 120, 6)
        self.productos["B5"] = Producto("B5", "Lápiz de ojos", 80, 6)

        #LUGAR:C
        #FILAS:1 AL 5
        self.productos["C1"] = Producto("C1", "Delineador líquido", 95, 6)
        self.productos["C2"] = Producto("C2", "Delineador en gel", 100, 6)
        self.productos["C3"] = Producto("C3", "Máscara de pestañas", 150, 6)
        self.productos["C4"] = Producto("C4", "Pestañas postizas", 75, 6)
        self.productos["C5"] = Producto("C5", "Labial en barra", 90, 6)

        #LUGAR:D
        #FILAS:1 AL 5
        self.productos["D1"] = Producto("D1", "Labial líquido", 95, 6)
        self.productos["D2"] = Producto("D2", "Brillo labial", 85, 6)
        self.productos["D3"] = Producto("D3", "Perfilador de labios", 70, 6)
        self.productos["D4"] = Producto("D4", "Spray fijador", 110, 6)
        self.productos["D5"] = Producto("D5", "Prebase para ojos", 105, 6)

        #LUGAR:E
        #FILAS:1 AL 5
        self.productos["E1"] = Producto("E1", "Prebase para rostro", 130, 6)
        self.productos["E2"] = Producto("E2", "Tinte para mejillas", 115, 6)
        self.productos["E3"] = Producto("E3", "Sombra de cejas", 90.0, 6)
        self.productos["E4"] = Producto("E4", "Gel para cejas", 95, 6)
        self.productos["E5"] = Producto("E5", "Lápiz para cejas", 85, 6)

        #LUGAR:F
        #FILAS:1 AL 5
        self.productos["F1"] = Producto("F1", "Paleta de sombras", 180, 6)
        self.productos["F2"] = Producto("F2", "Paleta de iluminadores", 170, 6)
        self.productos["F3"] = Producto("F3", "Paleta de rubores", 160, 6)
        self.productos["F4"] = Producto("F4", "Tónico facial", 140, 6)
        self.productos["F5"] = Producto("F5", "Aceite facial", 150, 6)

        #LUGAR:G
        #FILAS:1 AL 5
        self.productos["G1"] = Producto("G1", "Crema hidratante con color", 135, 6)
        self.productos["G2"] = Producto("G2", "Polvo matificante", 125, 6)
        self.productos["G3"] = Producto("G3", "Maquillaje mineral", 145, 6)
        self.productos["G4"] = Producto("G4", "Esmalte de uñas", 60, 6)
        self.productos["G5"] = Producto("G5", "Desmaquillante", 100, 6)

        #LUGAR:H
        #FILAS:1 AL 5
        self.productos["H1"] = Producto("H1", "Toallitas desmaquillantes", 75, 6)
        self.productos["H2"] = Producto("H2", "Pinceles de maquillaje", 180, 6)
        self.productos["H3"] = Producto("H3", "Esponjas de maquillaje", 90, 6)
        self.productos["H4"] = Producto("H4", "Kit de contorno", 190, 6)
        self.productos["H5"] = Producto("H5", "Pestañas postizas magnéticas", 120, 6)

##################################################################################################################
    def mostrar_productos_disponibles(self):
        
    #Muestra todos los productos disponibles en la máquina

        print("=== PRODUCTOS DISPONIBLES===")

        productos_diisponibles=0
        
        for codigo, producto in self.productos.items():
        #self.productos: es un diccionario("A1")
        #.items(): permite acceder tanto al codigo como al objeto producto en cada blcle(interaccion)

            if producto.tiene_stock(): #verifica si hay mas unidades(productos)disponibles
                 print(producto) #llama automarticamente al metodo __str__() del objeto producto
                 productos_disponibles += 1
 
                 if productos_disponibles == 0: #Si ningún producto tenía stock(cantidad de productos disponibles), se muestra este mensaje para informar al usuario.
                     print("No hay productos disponibles en este momento.")

        # El bucle for recorre el diccionario:
        # - codigo será "A1", "A2", etc.
        # - producto será el objeto Producto correspondiente
    ##################################################################################################################
    def insertar_dinero(self, cantidad):
       #Funcion que valida y permite al usuario insertar dinero en la maquina expendedora
        if cantidad > 0: #Verifica que la cantidad sea mayor a 0
            self.dinero_insertado += cantidad #Acumulador de dinero insertado
            print(f"Has insertado ${cantidad:.2f}")#Muestra el dinero insertado por ultima vez
            print(f"Total insertado: ${self.dinero_insertado:.2f}") #Muestra todo el dinero insertado
            return True
        else:
            print("La cantidad debe ser mayor que cero.") #Mensaje de error
            return False
        pass
    
    def mostrar_dinero_insertado(self):
 
        print(f"Dinero insertado: ${self.dinero_insertado:.2f}")#Solo muestra el dinero insertado con formato de moneda
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
      #Esta funcion permite regresarle el dinero al usuario en caso de cancelar la compra
        Dinero_devuelto = self.dinero_insertado
        if Dinero_devuelto > 0:
            print(f"Devolviendo ${Dinero_devuelto:.2f}")
            self.dinero_insertado = 0
        else:
            print("No es necesario dar cambio")
            
        pass
        #Codigo Descartado
   ################################################################################################# 
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