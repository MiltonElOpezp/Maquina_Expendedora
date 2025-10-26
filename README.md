# Proyecto Máquina Expendedora

## Descripción
Este proyecto implementa una máquina expendedora virtual que funciona en consola. El usuario puede insertar dinero, seleccionar productos, recibir cambio y realizar compras.

## Estructura del Proyecto

```
Maquina_Expendedora/
├── Main.py                    # Archivo principal para ejecutar
├── producto.py               # Clase Producto
├── maquina_expendedora.py    # Lógica principal de la máquina
├── utilidades.py            # Funciones auxiliares
├── menu.py                  # Interfaz de usuario y menús
└── README.md               # Este archivo
```

## Funcionalidades a Implementar

### 1. Clase Producto (`producto.py`)
- ✅ Estructura básica creada con comentarios
- ✅ Implementar constructor
- ✅ Implementar verificación de stock
- ✅ Implementar compra (reducir stock)
- ⏳ Implementar reposición de stock
- ✅ Implementar representación en string

### 2. Utilidades (`utilidades.py`)
- ✅ Estructura básica creada con comentarios
- ✅ Validar números positivos
- ✅ Validar códigos de productos
- ⏳ Formatear precios
- ✅ Limpiar pantalla
- ✅ Mostrar título
- ✅ Función de pausa

### 3. Máquina Expendedora (`maquina_expendedora.py`)
- ✅ Estructura básica creada con comentarios
- ✅ Implementar constructor
- ✅ Cargar productos iniciales
- ✅ Mostrar productos disponibles
- ✅ Insertar dinero
- ✅ Seleccionar y comprar productos
- ✅ Sistema de cambio/vuelto
- ✅ Devolver dinero
- ⏳ Modo administrador
- ⏳ Gestión de inventario

### 4. Menú e Interfaz (`menu.py`)
- ✅ Estructura básica creada con comentarios
- ✅ Menú principal
- ✅ Procesamiento de opciones
- ⏳ Menú de administrador
- ✅ Bucle principal del programa

## Orden de Implementación Sugerido

1. **Empezar con `producto.py`** - Es la clase más simple, ejemplos claros
2. **Continuar con `utilidades.py`** - Funciones que usarás en otros módulos
3. **Implementar `maquina_expendedora.py`** - La lógica principal con diccionarios
4. **Finalizar con `menu.py`** - La interfaz de usuario y bucles
5. **Probar desde `Main.py`** - Descomenta la línea de ejecución

## 📚 Conceptos de Programación que Aprenderás

- **Clases y objetos**: Crear y usar la clase Producto
- **Diccionarios**: Almacenar productos con código como clave
- **Validaciones**: Verificar entradas del usuario
- **Bucles while**: Mantener el programa ejecutándose
- **Condicionales if/elif**: Manejar opciones del menú
- **Manejo de excepciones**: try/except para validar números
- **Formateo de strings**: Mostrar precios y mensajes bonitos

## Productos Sugeridos para Cargar

```
A1: Coca Cola - $1.50 (10 unidades)
A2: Pepsi - $1.50 (8 unidades)
B1: Papas Lays - $2.00 (15 unidades)
B2: Doritos - $2.25 (12 unidades)
C1: Chocolate Kit Kat - $1.75 (6 unidades)
C2: Chicles Trident - $0.75 (20 unidades)
```

## Características del Sistema

- 💰 **Manejo de dinero**: Insertar, validar, devolver cambio
- 📦 **Control de stock**: Verificación automática de disponibilidad
- 🔐 **Modo administrador**: Gestión de inventario y reposición
- ✅ **Validaciones**: Entrada de usuario segura y robusta
- 🎯 **Interfaz clara**: Menús fáciles de usar y navegación intuitiva

## Cómo Probar

1. Implementa todas las funciones siguiendo los comentarios
2. En `Main.py`, descomenta la línea `ejecutar_maquina_expendedora()`
3. Ejecuta el programa desde la terminal:
   ```
   python Main.py
   ```

## Notas para el Desarrollo

- Todos los archivos tienen comentarios detallados explicando qué implementar
- Las funciones están estructuradas pero vacías (solo `pass`)
- Sigue los comentarios TODO para implementar cada función
- Prueba cada módulo por separado antes de integrar todo

¡Feliz programación! 🚀