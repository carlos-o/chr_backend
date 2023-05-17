# CHR-Backend

###### _Created on: 15/05/2023_

### Ejecución del proyecto

---

#### **Pre-requisitos**

- Tener instalado Python 3. (**Clic para descargar [Python](https://www.python.org/downloads/)** )
- Instalar el entorno virtual para el control de paquetes de un proyecto usando el siguiente comando:

  ```
      pip install virtualenv
  ```

> El gestor de paquetes ya está en Windows, sin embargo en Linux es necesario descargarlo.  
> Al hacer clic en el siguiente enlace se puede descargar [PIP](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers)

- Descarga de repositorios:
  credit-backend (backend)

#### **Paso 1. Creación y activación del entorno virtual**

---

**1.- Crear el entorno virtual**

Acceder a la terminal / consola de comando y utilizar:

        virtualenv -p python3 venv

> Al final del comando puede escribirse un nombre cualquiera, en este caso se utilizó el nombre venv

Con este comando se crea una carpeta para el entorno virtual que no está incluida en el proyecto con el nombre asignado, **_venv_** en este caso, y **de esta forma queda establecido el entorno virtual**.

**2.- Activar el entorno virtual**

Acceder a la carpeta, con el nombre asignado (**_venv_**), desde la terminal / consola de comandos y utilizar:

```Bash
Source bin/activate  (Linux)
Scripts/activate  (Windows)
```

> Para salir usar el comando deactivate dentro de la carpeta (**_venv_**)

**3.- Instalar las librerías dentro del entorno virtual**

Ejecutar el siguiente comando:

        pip install -r requirements.txt

Con este comando se instalan todas las librerías del repositorio dentro del entorno virtual para ejecutar el proyecto.

### **Paso 2. Creación de una base de datos**

---

_Crear una base de datos local en PostgreSQL._

> Debe coincidir la información de la base de datos y usuario de **PostgreSQL** con el archivo .env

### **Paso 3. Migración de la Data**

---

1.- Crear un archivo .env dentro de la raíz del proyecto y organizarlo dentro de la carpeta src.

2.- Abrir el archivo .env, copiar y pegar los siguientes datos:

    DEBUG=true
    URL=http://127.0.0.1:8000
    FRONT_URL=http://127.0.0.1:3000/
    SECRETKEY=django-secret-key
    DB_HOST=db
    DB_PORT=5432
    DB_NAME=app
    DB_USER=postgres
    DB_PASSWORD=supersecretpassword
    POSTGRES_DB=app
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=supersecretpassword


3.- Modificar los datos necesarios. La información más importante que debe ser modificada para ejecutar el proyecto es la mencionada debajo:

    DEBUG=true
    URL=http://127.0.0.1:8000
    FRONT_URL=http://127.0.0.1:3000/
    SECRETKEY=django-secret-key
    DB_HOST=db
    DB_PORT=5432
    DB_NAME=app
    DB_USER=postgres
    DB_PASSWORD=supersecretpassword
    POSTGRES_DB=app
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=supersecretpassword

### **Paso 4. Creación de superuser en Django**

---

Para acceder al admin de Django se debe crear un superuser (o superusuario) con el comando:

        python manage.py createsuperuser

### **Paso 5. Activación del server**

---

1.- Encender el server.

2.- Iniciar el server con el siguiente comando:

        python manage.py runserver

> Usar el url que proporciona el server y agregarle **/admin** al final para ingresar a credit-backend como admin. Debajo se muestra un ejemplo.

    http://127.0.0.1:8000/admin


#### **Creación y activación del entorno via docker**

1.- instalar docker [DOCKER](https://www.docker.com/)

2.- instalar docker compose [DOCKER-COMPOSE](https://docs.docker.com/compose/install/)

2.- ejecutar el comando:

        docker compose build

3.- ejecutar el comando

        docker compose up

4.- crear un superusuario para entrar al admin

        docker exec -it chr_app sh
        python manage.py createsuperuser

### **Paso 6. insercion de datos**

1.- para llenar la tablas de la app de network es necesario conocer el id del objeto network a guardar

       http://localhost:8000/network/bikerio 
llamando a la siguiente url se puede insertar los datos en las tablas correspondientes.

El servidor respondera acorde si existe o no el obejeto en la base de datos.

2.- ejecutar comando para la ejecucion del scraper y creación del json
* inicialmente se debera entrar al contendor 

        docker exec -it chr_app sh
        python manage.py scraper
 con este comando se realizar el proceso de obtener los datos de la pagina [snifa](https://snifa.sma.gob.cl/Sancionatorio/Resultado)
para luego almacenarlos en una json.

* Ejecutar el siguente comando para almacenar la informacion

        python manage.py jsonstore
para almacenar los datos obtenido en el scrpaer en la tabla correspondiente.

# NOTA
* Todos los modelos se pueden consultar en el administrador de django es necesario crear un superuser para visuralizar