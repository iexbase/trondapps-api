<img src="https://downloader.disk.yandex.ru/preview/1f688888f930c00e8afb606a492797b54e9438d43f843e86d97b341da925e7ac/5bcfa12a/fAJlD2l5xgfbrwqcVrk3P-I34t3RcHWHokWS-6T_RyBKrEjv10zua2KYWJDr3xEnekOZz7sKW4Xw7wKH7Quxmg%3D%3D?uid=0&filename=2018-10-23_21-30-19.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&size=2048x2048">

# trondapps-backend

## Install

* pip install djangorestframework, markdown, django-filter, django-cors-headers, unidecode, djongo
* configure file **/dapps/settings.py**
------
* python manage.py collectstatic
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver 8000

```python
# change params

CORS_ORIGIN_WHITELIST = ()
CORS_ORIGIN_REGEX_WHITELIST = ()
ALLOWED_HOSTS = []

# recommended not to change
CORS_ALLOW_METHODS = () 

```python 
# default database mongodb
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'tronapps',
    }
}
```

