# Django + Bootstrap

Aplicación de ejemplo desarrollada con Django y Twitter bootstrap.

## Librerias utilizadas:
* [Django 1.4.3] (http://www.djangoproject.com)
* [ReportLab Toolkit] (http://www.reportlab.com/software/opensource/)
* [Sqlite3] (http://www.sqlite.org/)
* [jQuery 1.8.3] (http://jquery.com/)
* [Twitter Bootstrap 2.2.2] (http://twitter.github.com/bootstrap/)
* [Bootstrap DatePicker] (http://www.eyecon.ro/bootstrap-datepicker/)

## Configuración
* Instalar ReportLab si no lo tiene instalado.

```
$ sudo pip install reportlab
```

* Luego comprobar en la consola de python si se instaló correctamente (Si no da errores al hacer el import)

```
$ import reportlab
```

* Configurar la base de datos

```
$ python manage.py syncdb
```
* Iniciar el servidor

```
$ python manage.py runserver
```
