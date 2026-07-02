# Sistema de Gestión de Productos

Proyecto Final desarrollado para **Talento Tech**.

## Descripción

Aplicación de consola desarrollada en Python para administrar un inventario de productos utilizando una base de datos SQLite.

El sistema permite realizar las operaciones básicas de un CRUD (Create, Read, Update, Delete) mediante un menú interactivo, validando los datos ingresados por el usuario y gestionando las transacciones sobre la base de datos.

## Funcionalidades

* Agregar productos.
* Consultar el listado completo de productos.
* Actualizar productos por ID o por nombre.
* Eliminar productos por ID o por nombre.
* Validación de los datos ingresados por el usuario.
* Manejo de excepciones y transacciones para garantizar la integridad de la base de datos.

## Tecnologías utilizadas

* Python 3.12 o superior.
* SQLite3 (incluido en la biblioteca estándar de Python).

## Estructura del proyecto

```
.
├── main.py
├── menu.py
├── crud.py
├── transaccion.py
├── utils.py
├── productos.db
└── README.md
```

### Descripción de los módulos

* **main.py**: punto de entrada de la aplicación. Crea la conexión con la base de datos, genera la tabla si no existe e inicia el menú principal.
* **menu.py**: contiene el menú principal y controla el flujo general del programa.
* **crud.py**: implementa las operaciones de alta, consulta, modificación y eliminación de productos, así como la interacción con el usuario.
* **transaccion.py**: concentra las operaciones SQL y el manejo de transacciones sobre la base de datos.
* **utils.py**: contiene funciones auxiliares para validar los datos ingresados por el usuario.

## Base de datos

La aplicación utiliza una base de datos SQLite llamada **productos.db**.

Si la base de datos o la tabla **productos** no existen, se crean automáticamente al iniciar el programa.

## Ejecución

Ubicarse en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 main.py
```

## Autor

Proyecto desarrollado como trabajo final para **Talento Tech**.
