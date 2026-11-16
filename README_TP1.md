Trabajo Práctico 1: ABM de Usuarios y Libros con FastAPI

---

Instalación de Dependencias y Ejecución

1. Crear y activar un entorno virtual:
   * Windows (PowerShell):
     ```bash
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   * Linux / macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

2. Instalar las dependencias:
   ```bash
   pip install "fastapi[standard]"
   ```

3. Levantar la aplicación:
   ```bash
   fastapi dev main.py
   ```
   El servidor local quedará escuchando por defecto en `http://127.0.0.1:8000`.

---

Acceso a la Documentación Interactiva (Swagger)

Con el servidor corriendo, abre tu navegador web e ingresa a la siguiente dirección para visualizar y probar todos los endpoints de forma interactiva:

http://127.0.0.1:8000/docs

¿Cómo probar los endpoints desde Swagger?
1. Haz clic sobre cualquiera de las rutas desplegadas (`GET`, `POST`, `PUT`, `DELETE`) para expandirla.
2. Presiona el botón **"Try it out"** ubicado a la derecha.
3. Completa los parámetros o el cuerpo JSON requerido (en caso de `POST` o `PUT`).
4. Haz clic en **"Execute"** para enviar la petición y observar el código de respuesta HTTP y los datos devueltos.

---

Endpoints Implementados

Parte 1 — Usuarios (`/user`)
* **`GET /user`**: Lista todos los usuarios. Permite filtrar por estado mediante el query param opcional `?is_active=true` o `?is_active=false`.
* **`POST /user`**: Crea un nuevo usuario (`id`, `name`, `is_active`).
* **`PUT /user/{id}`**: Actualiza los datos de un usuario existente por su ID.
* **`DELETE /user/{id}`**: Elimina un usuario existente por su ID.

### Parte 2 — Libros (`/libro`)
* **`GET /libro`**: Lista todos los libros. Permite filtrar por disponibilidad mediante el query param opcional `?disponible=true` o `?disponible=false`.
* **`POST /libro`**: Registra un nuevo libro (`id`, `titulo`, `autor`, `paginas`, `disponible`).
* **`PUT /libro/{id}`**: Actualiza los datos de un libro existente por su ID.
* **`DELETE /libro/{id}`**: Elimina un libro existente por su ID.