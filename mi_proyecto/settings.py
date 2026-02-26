import os
from pathlib import Path

# 1. DEFINICIÓN DE RUTAS (Debe ir arriba para evitar NameError)
# ----------------------------------------------------------------      
BASE_DIR = Path(__file__).resolve().parent.parent


# 2. CONFIGURACIÓN DE SEGURIDAD
# ----------------------------------------------------------------
SECRET_KEY = 'django-insecure-tu-llave-aqui'

DEBUG = True

# Permitimos todos los hosts para que funcione con 0.0.0.0
ALLOWED_HOSTS = ['*']


# 3. DEFINICIÓN DE APLICACIONES
# ----------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Proyecto', # Tu App de artículos
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mi_proyecto.urls'

# 4. CONFIGURACIÓN DE TEMPLATES (Corregida con la ruta de tu carpeta)
# ----------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Proyecto' / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mi_proyecto.wsgi.application'


# 5. BASE DE DATOS (Conexión a XAMPP / MariaDB)
# ----------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Proyecto',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# 6. VALIDACIÓN DE CONTRASEÑAS Y LENGUAJE
# ----------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# 7. ARCHIVOS ESTÁTICOS Y CAMPOS POR DEFECTO
# ----------------------------------------------------------------
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'