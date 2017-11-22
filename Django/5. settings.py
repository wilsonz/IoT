# since settings.py generated from the command 'django-admin startproject' contains SECRET_KEY
# and other import settings, only insert the code highlighted in bold and keep all other

...
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.160']           --> add IP addresses
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',                                  --> add your app name
]
...
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   --> change database from sqlite3 to mysql
        'NAME': 'stevens',
        'USER': 'pi',
        'PASSWORD': 'PASSWORD',              
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
...
TIME_ZONE = 'America/New_York'                --> change time from UTC to America/New_York
...
