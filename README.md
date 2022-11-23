# django_celery
Proyecto demo usando Django y Celery del curso [Tareas Asíncronas y Programadas Utilizando Django/Celery/RabbitMQ](https://coderslink.com/talento/tutoriales-de-programacion/tareas-asincronas-con-django-celery-rabbitmq/on-demand/)

Celery es un gestor de tareas distribuido y asíncrono desarrollado en Python. Es una herramienta magnífica para aplicaciones de alta disponibilidad y con alta carga.

## Descripción
- Se envían correos al agregarse un nuevo subscritor, nueva publicación.

- Se agregó un archivo de configuración de celery en el directorio `django_celery` llamado [celery.py](django_celery/celery.py)

- Se importó la app de celery sobre el archivo [__init__.py](django_celery/__init__.py)

- Fue agregado un archivo en el directorio `apps/network` con las tareas o tasks de celery con el nombre [tasks.py](apps/network/tasks.py)

- Se reemplazó el llamado a las funciones para enviar correos en el archivo [signals.py](apps/network/signals.py) por las nuevas tasks

- Ahora se ejecutará el envío de correos de manera asíncrona

- Se agregó la configuración en el settings para ejecutar tasks con celery beat
- Dos tasks fueron agregadas:
    - Eliminar logs cada 5 segundos, dejando los últimos 10
    - Enviar un mensaje de inicio de semana los lunes a las 8:00 am

## Correr proyecto
1. Crear archivo .env con base al archivo ejemplo .env.example para poder cargar la configuración de la base de datos.
    ```bash
    $ cp .env.example .env
    ```
2. Instalar dependencias.
    ```bash
    $ pip install -r requirements.txt
    ```
3. Aplicar migraciones.
    ```bash
    $ python manage.py migrate
    ```
4. Crear super usuario.
    ```bash
    $ python manage.py createsuperuser
    ```
4. Iniciar servidor.
    ```bash
    $ python manage.py runserver
    ```

## Pasos para usar Celery
1. Instalar Celery:

~~~
pip install celery # paquete directamente
pip install -r requirements.txt # paquete desde el requirements.txt
~~~
2. Instalar RabbitMQ. Puedes revisar la [Documentación oficial](https://www-rabbitmq-com.translate.goog/download.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es-419&_x_tr_pto=sc)

    Para este ejemplo vamos a correrlo con docker:

    `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management`


3. Iniciar un worker de Celery:

    ~~~
    celery -A django_celery worker -l INFO # Levantar 1 worker

    celery -A django_celery worker -l INFO --concurrency=1 -n worker1@%h # Levantar 1 worker con concurrencia y asignandole 1 nombre: worker1, %h es para indicar el nombre del host
    ~~~

4. Para ejecutar las tareas de Celery Beats es necesario ejecutar:
    `celery -A django_celery beat`

5. Para monitorear las tareas utilizaremos podemos utilizar el monitor de Celery o el paquete Flower:
    - Celery: `celery -A django_celery events`
    - [flower](https://flower.readthedocs.io/en/latest/index.html):
    ~~~
        pip install flower # Instalar
        celery flower -A django_celery --port=5555 # Iniciar flower
        http://localhost:5555 # Acceder
    ~~~
