# Documentación Técnica: Desarrollo de App Django

Este documento detalla los pasos seguidos para la construcción de la aplicación de gestión de artículos.

## I Ambiente Virtual y Librerías
- Creación del entorno: `python -m venv venv`.
- Activación: `.\venv\Scripts\activate` (Windows).
- Librerías: `pip install django mysqlclient`.

## II Creación del Proyecto y Base de Datos
- Comando: `django-admin startproject mi_proyecto`.
- Habilitación de DB: Configuración de la sección `DATABASES` en `settings.py` apuntando a MySQL en el puerto 3306 (XAMPP).

## III Creación de App y Settings
- Comando: `python manage.py startapp Proyecto`.
- Modificación de Settings: Se agregó `'Proyecto',` a la lista de `INSTALLED_APPS`.

## IV Estructura de Archivos
- `mi_proyecto/`: Configuración global del proyecto.
- `Proyecto/`: Lógica de la aplicación (Models, Views, Forms).
- `templates/`: Archivos HTML organizados por carpetas.
- `manage.py`: Administrador de comandos de Django.

## V Pasos para Probar Modificaciones
1. Asegurar que MySQL esté activo en XAMPP.
2. Ejecutar migraciones: `python manage.py makemigrations` y `python manage.py migrate`.
3. Iniciar servidor: `python manage.py runserver`.
4. Verificar en el navegador mediante `127.0.0.1:8000`.

## VI Listado de Entidades (MVT)
- **Vista**: Uso de `ListView` en `views.py` para recuperar todos los objetos.
- **URL**: Mapeo en `urls.py` hacia `path('all', views.ArticleListView.as_view(), name="all_articles")`.
- **Template**: Uso de bucle `{% for article in articles_list %}` en el HTML.

## VII Generación de Nueva Entidad
- **Formulario**: Creación de clase en `forms.py` basada en `ModelForm`.
- **Vista**: Implementación de lógica `POST` para guardar datos mediante `form.save()`.
- **URL**: Habilitación de la ruta `/new` para acceder al formulario de registro.

---
**Referencias:**
- Documentación oficial de Django: [docs.djangoproject.com](https://docs.djangoproject.com/)
- Tutoriales de Python Software Foundation.