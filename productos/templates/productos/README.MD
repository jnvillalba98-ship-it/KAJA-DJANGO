# KAJA

Sistema de Gestión de Inventario desarrollado como evidencia del programa **Tecnólogo en Análisis y Desarrollo de Software (ADSO)** del SENA.

## Descripción

KAJA es una aplicación web desarrollada con Django que permite administrar el inventario de pequeños y medianos negocios mediante un módulo CRUD de productos.

El sistema facilita el registro, consulta, actualización y eliminación de productos, permitiendo mantener un control organizado del inventario.

## Objetivo

Desarrollar una aplicación web que implemente operaciones CRUD sobre una base de datos MySQL, aplicando el patrón Modelo-Vista-Plantilla (MVT) de Django y utilizando Bootstrap para el diseño de la interfaz.

## Tecnologías utilizadas

- Python 3.13
- Django 6
- MySQL
- Bootstrap 5
- HTML5
- CSS3
- Visual Studio Code
- DBeaver
- Laragon
- Git
- GitHub

## Funcionalidades

- Registro de productos.
- Consulta de productos.
- Edición de productos.
- Eliminación de productos.
- Gestión de inventario.
- Búsqueda por código y nombre.
- Dashboard con estadísticas.
- Paginación de registros.
- Mensajes de confirmación.

## Base de datos

Nombre:

```
kaja
```

Tabla principal:

```
productos_producto
```

Campos:

- id
- codigo
- nombre
- descripcion
- precio
- stock
- activo
- fecha_creacion

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar migraciones:

```bash
python manage.py migrate
```

Iniciar el servidor:

```bash
python manage.py runserver
```

## Autor

Proyecto desarrollado por:

**Tu nombre**

Tecnólogo en Análisis y Desarrollo de Software

Servicio Nacional de Aprendizaje - SENA