## Proyecto de API Candidatos

**Descripción:**

Este proyecto de API de candidatos está desarrollado con FastAPI, SQLAlchemy y SQLite. La API permite:

-   Agregar nuevos candidatos a una base de datos SQLite.
-   Obtener una lista de todos los candidatos almacenados.

**Configuración del entorno:**

1.  Asegúrate de tener Python instalado en tu sistema.
2.  Instala las dependencias del proyecto con el siguiente comando:

```
pip install -r requirements.txt

```

**Ejecución de la aplicación:**

1.  Inicia el servidor de desarrollo desde la carpeta raíz con el siguiente comando:

```
uvicorn app.main:app --reload

```

2.  El servidor se iniciará en http://localhost:8000.

**Endpoints:**

**1. Crear un nuevo candidato:**

-   **Método:**  POST
-   **URL:**  http://localhost:8000/candidato
-   **Datos:**  JSON con los siguientes campos:
    -   `dni`: Número de identificación del candidato (string).
    -   `nombre`: Nombre del candidato (string).
    -   `apellido`: Apellido del candidato (string).

Por ejemplo:

JSON

```
{
  "dni": "12345678",
  "nombre": "Juan",
  "apellido": "Perez"
}
```

**2. Obtener todos los candidatos:**

-   **Método:**  GET
-   **URL:**  http://localhost:8000/candidato

**Nota sobre DNI duplicado:**

La API verifica si el DNI proporcionado al crear un nuevo candidato ya existe en la base de datos. Si se detecta un DNI duplicado, se devuelve un error 400 (BadRequest) con el mensaje "DNI duplicado".

**Base de datos:**

La aplicación utiliza una base de datos SQLite para almacenar los candidatos. La configuración de la base de datos se encuentra en el archivo `main.py`.