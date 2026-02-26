# Sistema de Gestión de Artículos - Django & MySQL

Este proyecto es una aplicación web desarrollada en Django que permite realizar operaciones CRUD completas sobre una base de datos MySQL (XAMPP).

## Pasos de Configuración e Instalación
1. **Entorno**: Creación de ambiente virtual e instalación de Django y mysqlclient.
2. **Base de Datos**: Configuración de conexión a MySQL en settings.py y ejecución de migraciones.
3. **Estructura MVT**:
   - Modelos: Definición de la entidad Article.
   - Vistas: Uso de ListView para el catálogo y DetailView para el detalle individual.
   - Formularios: Implementación de ModelForm para creación y edición.
4. **Templates**: Sistema de plantillas con herencia (base.html) y Bootstrap 5.

## Funcionalidades Implementadas
- Listado general de artículos (/articles/all).
- Visualización de detalle por ID (/articles/<id>).
- Creación de nuevos artículos (/articles/new).
- Edición de artículos existentes (/articles/edit/<id>).

Desarrollado por: Alan