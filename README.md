# Django Rest Framework

La plantilla de Django Rest Framework es útil para projectos con múltiples _CRUDs_, permite generar endpoints de manera muy rápida y fácil de probar.
### Features
* Postgres configurado
* Autenticación por JWT

# Uso
Para utilizar esta plantilla, ejecuta los siguientes comandos:
```bash
python -m venv <ENV_NAME>
source <ENV_NAME>/bin/activate
# En windows: env/Scripts/activate
pip install django
django-admin startproject --template=https://github.com/percept-io/templates/archive/drf.zip <PROJECT_NAME>
```

Con esto, se cuenta con un proyecto de Django Rest Framework, utilizando un modelo _Custom_ de usuario, para que sea más fácil modificarlo, y Autenticación por JWT.

Para terminar de configurar, es necesario modificar algunas variables de ambiente al archivo _app/.env_, así cómo crear la base de datos en postgres.

```
SECRET_KEY=<RANDOM_STRING>
DB_NAME=<DATABASE_NAME>
DB_USER=<DATABASE_USER>
DB_PWD=<DATABASE_USER_PASSWORD>
```

Teniendo las configuraciones necesarias, es necesario instalar las dependencias, y ejecutar las migraciones pendientes:

```bash
cd <PROJECT_NAME>
pip install -r requirements.txt
python manage.py migrate
```

Con las dependencias instaladas y la base de datos lista, se puede crear un usuario y empezar a utilizar el proyecto:
```bash
python manage.py createsuperuser
# Crea tu usuario con el correo y contraseña
python manage.py runserver
```

[Regresar al índice](https://github.com/percept-io/templates/tree/master)
