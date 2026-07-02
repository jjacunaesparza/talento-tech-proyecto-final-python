# Modulo para el menu principal.


from crud import agregar, consultar, actualizar, borrar


# MOSTRAR EL MENU PRINCIPAL
def menu(cursor,conexion) -> None:
    """
    Menu de opciones.
    Parametros: 
        cursor: objeto que actúa como intermediario entre el programa y la base de datos.
        conexion: objeto que representa la conexión abierta con la base de datos.
    Retorna:
        (nada)
    """

    while True:
        print("\n\n" + "*" * 50)
        print("*** Sistema de Gestion de Inventario y Precios ***")
        print("*" * 50)
        print("\nBienvenidos!\n")
        print("1 - Agregar Producto")
        print("2 - Mostrar")
        print("3 - Actualizar")
        print("4 - Eliminar")
        print("5 - Salir")

        opcion = input("\nIngrese el numero de opcion: ").strip()
        print("\n")

        match opcion:
            case "1":
                agregar(cursor,conexion)

            case "2":
                consultar(cursor)

            case "3":
                actualizar(cursor,conexion)

            case "4":
                borrar(cursor,conexion)

            case "5":
                print("🔄️ Gracias por utilizar nuestro Sistema! Hasta luego!")
                conexion.close()
                break

            case _:
                print("⛔ Error en el ingreso de los datos, intente nuevamente.")