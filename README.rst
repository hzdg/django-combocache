django-combocache
---------------

![ComboCache](http://slice.seriouseats.com/images/20100721-combos-pizzeriapretzel.jpg)

Installation
===============

``pip install -e git@github.com:hzdg/django-combocache.git#egg=django-combocache``


About
===============

Simple cache backend for using multiple cache backends with a ranked fallback sequence.


Use
===============

Add the following to your `CACHES` setting:

```python
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'TIMEOUT': 60 * 30,
            'KEY_PREFIX': 'warm-milk-'
        },
        'filebased': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/path/to/cache/folder',
        },
        'tester': {
            'BACKEND': 'combocache.ComboCache',
            'CACHES': ['default', 'filebased']
        }
    }
```
