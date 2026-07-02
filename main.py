"""
Archivo principal del proyecto.

Ejecutar este archivo para iniciar la aplicación.
"""


# Proyecto Final
"""
Base de datos: Crear una base de datos llamada 'inventario.db' para almacenar los datos de los productos. La
tabla 'productos' debe contener las siguientes columnas:

    - 'id': Identificador único del producto (clave primaria, autoincremental).
    - 'nombre': Nombre del producto (texto, no nulo).
    - 'descripcion': Breve descripción del producto (texto).
    - 'cantidad': Cantidad disponible del producto (entero, no nulo).
    - 'precio': Precio del producto (real, no nulo).
    - 'categoria': Categoría a la que pertenece el producto (texto).

Funcionalidades de la aplicación. La aplicación debe permitir:

    - Registrar nuevos productos.
    - Visualizar datos de los productos registrados.
    - Actualizar datos de productos, mediante su ID.
    - Eliminación de productos, mediante su ID.
    - Búsqueda de productos, mediante su ID. De manera opcional, se puede implementar la búsqueda por los
    campos nombre o categoría.
    - Reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario o
    usuaria.

Interfaz de usuario:

    Implementar una interfaz de usuario básica, para interactuar con la base de datos a través de la terminal.
    La interfaz debe incluir un menú principal con las opciones necesarias para acceder a cada funcionalidad
    descrita anteriormente.
    Opcional: Utilizar el módulo 'colorama' para mejorar la legibilidad y experiencia de usuario en la terminal,
    añadiendo colores a los mensajes y opciones.

Requisitos técnicos:

    El código debe estar bien estructurado, utilizando funciones para modularizar la lógica de la aplicación.
    Los comentarios deben estar presentes en el código, explicando las partes clave del mismo.
"""


# Resolucion


import sqlite3
from menu import menu


def main() -> None:
    """
    Función principal del programa.
    Establece la conexión con la base de datos, crea la tabla de productos si no existe, invoca el menú
    principal y cierra la conexión al finalizar.
    Parametros:
        (ninguno)
    Retorna:
        (nada)
    """

    conexion = sqlite3.connect("productos.db")  # Establecer la conexión a la base de datos

    cursor = conexion.cursor()  # Crear un objeto cursor

    try:
        # Crear una tabla productos.db:
        cursor.execute(''' CREATE TABLE IF NOT EXISTS productos
                    (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    cantidad INT NOT NULL,
                    precio REAL NOT NULL,
                    categoria TEXT
                    )
                    ''')

        conexion.commit()

        menu(cursor,conexion)

    finally:  # Aca me aseguro que la conexión se cierre siempre, incluso si una excepción no controlada llega hasta main()
        conexion.close()

if __name__ == "__main__":
   main()