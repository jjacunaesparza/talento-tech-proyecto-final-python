# Modulo para las operaciones de Create, Read, Update y Delete que se muestran en el menu principal.
# Aqui se almacenan las funciones que manejan la lógica de interaccion con el usuario.


import utils
import transaccion as tra


# AGREGAR (CREATE)
def agregar(cursor, conexion) -> None:
    """
    Funcion para agregar un producto.
    Parametros: 
        cursor: objeto que actúa como intermediario entre el programa y la base de datos.
        conexion: objeto que representa la conexión abierta con la base de datos.
    Retorna:
        (nada)
    """
    while True:
        nombre = utils.validar_str("el nombre","guardar")

        cantidad = utils.validar_int("la cantidad")

        precio = utils.validar_float()

        categoria = utils.validar_str("la categoria","guardar")


        # Insertar datos en la tabla
        tra.agregar_en_tabla(cursor,conexion,nombre,cantidad,precio,categoria)
        
        mas_datos = input("\n✅ Datos guardados exitosamente! Desea ingresar mas datos? (s/n): ").lower().strip()

        if mas_datos != "s":
            return None



# CONSULTAR TODA LA BASE DE DATOS (READ)
def consultar(cursor) -> None:
    """
    Leer todos los elementos de la tabla productos.db.
    Parametros: 
        cursor: objeto que actúa como intermediario entre el programa y la base de datos.
        conexion: objeto que representa la conexión abierta con la base de datos.
    Retorna:
        (nada)
    """

    # Recuperar todos los registros de la tabla productos.db
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    
    print("\n=====   Lista de Productos   =====")
    
    for producto in productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1].title()}, Cantidad: {producto[2]}, Precio: $ {producto[3]:.2f}, Categoria: {producto[4].capitalize()}")



# ACTUALIZAR (UPDATE)
def actualizar(cursor, conexion) -> None:
    """
    Actualizar un producto de la tabla por ID o por nombre.
    Parametros:
        cursor: objeto que actúa como intermediario entre el programa y la base de datos.
        conexion: objeto que representa la conexión abierta con la base de datos.
    Retorna:
        (nada)
    """

    while True:
        opcion = input("Desea buscar por ID (ingrese '1') o por nombre de producto (ingrese '2')?: ").strip()

        match opcion:
            case "1":
                valor = utils.validar_int("el ID")
                campo = "id"

            case "2":
                valor = utils.validar_str("el nombre", "actualizar")
                campo = "nombre"

            case "":
                print("⛔ No se ingresó ninguna opción, volviendo al menú...")
                return None

            case _:
                print("⛔ Error en el ingreso de los datos, intente nuevamente.")
                continue

        # Buscar el producto
        producto = tra.buscar_producto(cursor,campo,valor)

        if producto is None:
            mas_datos = input(f"\n⛔ El {campo} no existe. Desea ingresar otro producto a actualizar? (s/n): ").lower().strip()
        else:
            print("\n===== Producto encontrado =====")
            print(f"ID: {producto[0]}")
            print(f"Nombre: {producto[1]}")
            print(f"Cantidad: {producto[2]}")
            print(f"Precio: $ {producto[3]:.2f}")
            print(f"Categoría: {producto[4]}")

            print("\nIngrese los nuevos datos:")

            nombre = utils.validar_str("el nombre","actualizar")
            cantidad = utils.validar_int("la cantidad")
            precio = utils.validar_float()
            categoria = utils.validar_str("la categoria","actualizar")

            filas_afectadas = tra.actualizar_en_tabla(cursor,conexion,producto[0],nombre,cantidad,precio,categoria)

            if filas_afectadas == -1:
                continue

            print("\n✅ Producto actualizado exitosamente!")

            mas_datos = input("Desea actualizar otro producto? (s/n): ").lower().strip()

        if mas_datos != "s":
            return None



# BORRAR (DELETE)
def borrar(cursor, conexion) -> None:
    """
    Borrar un producto de la tabla por ID o por nombre.
    Parametros: 
        cursor: objeto que actúa como intermediario entre el programa y la base de datos.
        conexion: objeto que representa la conexión abierta con la base de datos.
    Retorna:
        (nada)
    """

    while True:
        opcion = input("Desea eliminar por ID (ingrese '1') o por nombre de producto (ingrese '2')?: ").strip()

        match opcion:
            case "1":
                valor = utils.validar_int("el ID")
                campo = "id"
                filas_afectadas = tra.borrar_en_tabla(cursor,conexion,campo,valor)

            case "2":
                valor = utils.validar_str("el nombre","eliminar")
                campo = "nombre"
                filas_afectadas = tra.borrar_en_tabla(cursor,conexion,campo,valor)

            case "":
                print("⛔ No se ingresó ninguna opcion, volviendo al menu...")  # Si se presiona un <enter> vuelve al menu principal
                return None

            case _:
                print("⛔ Error en el ingreso de los datos, intente nuevamente.")
                continue

        if filas_afectadas == -1:  # Si es -1 hubo un error al registrar el cambio en la base de datos
            continue
        elif filas_afectadas == 0:  # Si es 0 el parametro de busqueda no existe
            mas_datos = input(f"\n⛔ El {campo} no existe. Desea ingresar otro producto a eliminar? (s/n): ").lower().strip()
        else:  # Si es cualquier otro valor se pudo eliminar el registro
            mas_datos = input("\n✅ Producto eliminado exitosamente! Desea eliminar mas datos? (s/n): ").lower().strip()

        if mas_datos != 's':
            return None