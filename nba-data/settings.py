import django_mongodb

DATABASES = {
   'default' : {
      'ENGINE' : 'django_mongodb_engine',
      'NAME' : 'stats_db',
   }
}

_MONGODB_USER = 'mongouser'
_MONGODB_PASSWD = 'password'
_MONGODB_HOST = 'thehost'
_MONGODB_NAME = 'thedb'
_MONGODB_DATABASE_HOST = \
   'mongodb://%s:%s@%s/%s' \
   % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)

django_mongodb_engine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)