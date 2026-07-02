# Modulo para las funciones de validacion de ingreso de datos.


# VALIDAR UN STRING
def validar_str(texto:str, accion:str) -> str:
    """
    Pide un texto al usuario y se asegura que no este vacio ni contenga numeros.
    Parametros:
        texto: string variable segun el campo de la tabla que se quiera validar.
        accion: string que indica lo que se hará con el dato ingresado (ej: guardar, borrar, etc ...).
    Retorna:
        texto: el string ingresado por el usuario, con validacion.
    """

    while True:
        cadena = input(f"Ingrese {texto} del producto a {accion}: ").strip().lower()
        if cadena == "" or not cadena.replace(" ","").isalpha():  # Filtro <enter> vacio y numeros, permitiendo nombres compuestos
            print(f"❌ Error en {texto}, intente nuevamente.")
        else:
            return cadena



# VALIDAR UN FLOAT
def validar_float() -> float:
    """
    Pide un numero decimal al usuario y se asegura que sea valido.
    Parametros:
        (nada)
    Retorna:
        valor: el float ingresado por el usuario, con validacion.
    """

    while True:
        valor = input("Ingrese el precio ($) = ").strip()

        try:
            valor = float(valor)
            if valor < 0:
                print("❌ Error en el ingreso del precio, intente nuevamente.")
                continue
            return valor

        except ValueError:
            print("❌ Error en el ingreso del precio, intente nuevamente.")



# VALIDAR UN INT
def validar_int(texto:str) -> int:
    """
    Pide un numero entero al usuario y se asegura que sea valido.
    Parametros:
        texto: string variable segun el campo de la tabla que se quiera validar.
    Retorna:
        valor: el int ingresado por el usuario, con validacion.
    """

    while True:
        valor = input(f"Ingrese {texto}: ").strip()

        try:
            valor = int(valor)
            if valor < 0:
                print(f"❌ Error en {texto}, intente nuevamente.")
                continue
            return valor

        except ValueError:
            print(f"❌ Error en {texto}, intente nuevamente.")