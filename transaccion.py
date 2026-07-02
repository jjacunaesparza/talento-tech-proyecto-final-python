# Modulo para las transacciones con la base de datos.


import sqlite3


# TRANSACCION PARA AGREGAR UN REGISTRO CON TODOS SUS CAMPOS
def agregar_en_tabla(cursor, conexion, nombre:str, cantidad:int, precio:float, categoria:str) -> None:
    """
    Funcion para agregar un registro y asegurar la correcta escritura en la tabla.
    Parametros: 
        cursor: objeto que actúa como intermediario entre el programa y la base de datos.
        conexion: objeto que representa la conexión abierta con la base de datos.
        nombre: string con el nombre del producto.
        cantidad: entero con la cantidad de articulos que se tiene en stock.
        precio: decimal con el precio del producto.
        categoria: string con la categoria a la que pertenece el producto.
    Retorna:
        (nada)
    """

    try:
        # Iniciar la transacción
        conexion.execute("BEGIN TRANSACTION")

        # Insertar el nuevo producto en la tabla
        cursor.execute('''INSERT INTO productos (nombre, cantidad, precio, categoria) VALUES
                    (?, ?, ?, ?)
                    ''',(nombre.title(),cantidad,precio,categoria.capitalize())
                    )

        # Confirmar los cambios
        conexion.commit()

    except sqlite3.Error as e:
        # Si ocurre un error, se revierten los cambios
        conexion.rollback()
        print(f"⛔ Error al registrar el producto: {e}")



# TRANSACCION PARA ACTAULIZAR UN REGISTRO POR ID O POR NOMBRE
def actualizar_en_tabla(cursor, conexion, campo:str, valor:int | str) -> int:
    """
    Funcion para actualizar un registro por ID o por nombre y asegurar la correcta escritura en la tabla.
    Parametros: 
        cursor: objeto que actúa como intermediario entre el programa y la base de datos.
        conexion: objeto que representa la conexión abierta con la base de datos.
        campo: string con el nombre de la columna por la que se buscará el registro a actualizar.
        valor: string o entero a buscar en la columna indicada.
    Retorna:
        cursor.rowcount: entero con la cantidad de filas que fueron afectadas en la ultima sentencia SQL ejecutada.
        -1 en caso que ocurra una excepcion
    """



# TRANSACCION PARA ELIMINAR UN REGISTRO POR ID O POR NOMBRE
def borrar_en_tabla(cursor, conexion, campo:str, valor:int | str) -> int:
    """
    Funcion para eliminar un registro por ID o por nombre y asegurar la correcta escritura en la tabla.
    Parametros: 
        cursor: objeto que actúa como intermediario entre el programa y la base de datos.
        conexion: objeto que representa la conexión abierta con la base de datos.
        campo: string con el nombre de la columna por la que se buscará el registro a eliminar.
        valor: string o entero a buscar en la columna indicada.
    Retorna:
        cursor.rowcount: entero con la cantidad de filas que fueron afectadas en la ultima sentencia SQL ejecutada.
        -1 en caso que ocurra una excepcion
    """

    try:
        # Iniciar la transacción
        conexion.execute("BEGIN TRANSACTION")

        # Borrar el producto de la tabla
        cursor.execute(f"DELETE FROM productos WHERE {campo} = ?", (valor,))

        if cursor.rowcount == 0:
            conexion.rollback()
        else:
            conexion.commit()

        return cursor.rowcount

    except sqlite3.Error as e:
        # Si ocurre un error, se revierten los cambios
        conexion.rollback()
        print(f"⛔ Error al registrar el cambio en la base de datos: {e}")
        return -1  # Se devuelve el valor -1 como indicador de error