# trondapps-backend

## Install

* pip install djangorestframework, markdown, django-filter, django-cors-headers, unidecode, djongo
* configure file **/dapps/settings.py**
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

