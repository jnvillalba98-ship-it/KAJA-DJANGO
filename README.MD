# KAJA

## Sistema de Gestión de Inventario

KAJA es una aplicación web desarrollada con **Django** y **MySQL** para la administración de productos e inventario de pequeños y medianos negocios.

Este proyecto fue desarrollado como evidencia **GA7-220501096-AA2-EV01** del programa **Tecnólogo en Análisis y Desarrollo de Software (ADSO)** del Servicio Nacional de Aprendizaje (SENA).

---

# Objetivo

Desarrollar un sistema web que permita administrar productos mediante operaciones CRUD (Crear, Consultar, Actualizar y Eliminar), facilitando el control del inventario de un negocio.

---

# Funcionalidades

- Registro de productos.
- Consulta de productos.
- Actualización de productos.
- Eliminación de productos.
- Gestión de inventario.
- Búsqueda por código y nombre.
- Dashboard con estadísticas.
- Paginación de registros.
- Validación de formularios.

---

# Tecnologías utilizadas

- Python 3
- Django
- MySQL
- Bootstrap 5
- HTML5
- CSS3
- Git
- GitHub
- Visual Studio Code
- DBeaver
- Laragon

---

# Arquitectura del proyecto

El proyecto sigue el patrón de arquitectura **MVT (Modelo - Vista - Plantilla)** propio de Django.

```
KAJA-DJANGO
│
├── kaja/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── productos/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# Base de datos

Motor:

- MySQL

Nombre de la base de datos:

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

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/kaja.git
```

## 2. Ingresar al proyecto

```bash
cd kaja
```

## 3. Crear el entorno virtual

```bash
python -m venv .venv
```

## 4. Activar el entorno virtual

Windows

```bash
.venv\Scripts\activate
```

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 6. Configurar la base de datos MySQL

Editar el archivo:

```
kaja/settings.py
```

Configurar:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kaja',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 7. Ejecutar migraciones

```bash
python manage.py migrate
```

## 8. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000/
```

---
## Acceso desde dispositivos móviles (desarrollo)

Para acceder a la aplicación desde un celular o una tablet conectados a la misma red Wi-Fi que el computador, sigue estos pasos:

### 1. Configurar `ALLOWED_HOSTS`

En el archivo `settings.py`:

```python
ALLOWED_HOSTS = ['*']
```

> **Nota:** Esta configuración es únicamente para desarrollo. En producción se deben especificar los dominios o direcciones IP permitidos.

### 2. Iniciar el servidor

Ejecuta el siguiente comando desde la carpeta donde se encuentra `manage.py`:

```bash
python manage.py runserver 0.0.0.0:8000
```

### 3. Obtener la dirección IP del computador

En Windows ejecuta:

```cmd
ipconfig
```

Busca la línea **Dirección IPv4**.

Ejemplo:

```text
Dirección IPv4 . . . . . . . . . : 192.168.1.6
```

### 4. Acceder desde el celular

Abre el navegador del dispositivo móvil y escribe:

```
http://192.168.1.6:8000
```

Reemplaza `192.168.1.6` por la dirección IPv4 de tu computador.

### Requisitos

- El computador y el celular deben estar conectados a la misma red Wi-Fi.
- El Firewall de Windows debe permitir conexiones al puerto **8000**.
- El servidor de Django debe estar en ejecución.

# Capturas del sistema

Aquí se pueden agregar imágenes de:

- Listado de productos.
- Registro de productos.
- Edición.
- Eliminación.
- Dashboard.

---

# Autor

Nicolas Villalba

Tecnólogo en Análisis y Desarrollo de Software

Servicio Nacional de Aprendizaje - SENA

2026
