import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kngepvxt6e582&9*-xvhcln0uo!k*^%tm_@5uw42inc-h@6$lh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
  'corsheaders',
  'whitenoise.runserver_nostatic',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  # 'cloudinary_storage'
  'cloudinary',
  'django.contrib.staticfiles',
  
  
  # 3rd party
  'rest_framework',
  

  # Local
  'about',
  'projects',
  'technologies',
  'testimonials',
  'contact',
  'hero',
  'footer',
]

MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'build')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': BASE_DIR / 'db.sqlite3',
#   }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ['DB_NAME_DJANGO'],
#         'USER': os.environ['DB_USER_DJANGO'],
#         'PASSWORD': os.environ['DB_PASSWORD_DJANGO'],
#         'HOST': os.environ['CLOUD_SQL_INSTANCE_IP'],
#         'PORT': 5432,
#     }
# }
# DATABASES = dj_database_url.config(default=os.environ['DATABASE_URL'])
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ['DATABASE_URL'],
    )
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
  },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dtjivws2c',
    'API_KEY': '897949739888447',
    'API_SECRET': '3fFPMLX_uRSUXR2noV-SmQXFP-s'
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# MEDIA_ROOT is for the user-uploaded content

# STATIC_URL = '/static/'
# STATIC_ROOT = '/opt/render/project/src/static/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
# MEDIA_URL = '/media/'
# MEDIA_ROOT = '/opt/render/project/src/media/'
MEDIA_URL = '/media/'  # or any prefix you choose
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_WHITELIST = [
  "http://localhost:3000",
  "https://ayushkrportfolio.onrender.com",
]
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
CORS_EXPOSE_HEADERS = [
    "Access-Control-Allow-Origin",
]
# CSRF_TRUSTED_ORIGINS = [
#     "https://ayushkrportfolio.onrender.com",
# ]



FILE_UPLOAD_PERMISSIONS=0o640