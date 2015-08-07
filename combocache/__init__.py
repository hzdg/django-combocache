from django.core.cache import get_cache
from django.core.cache.backends.base import BaseCache


class ComboCache(BaseCache):
    def __init__(self, server, params):
        cache_names = params.get('CACHES', None)
        if not cache_names:
            raise Exception("CACHES must include one or more cache backends")
        self.caches = [get_cache(cache_name) for cache_name in cache_names]

    def get(self, key, default=None, version=None):
        missed_caches = []
        for cache in self.caches:
            value = cache.get(key, version=version)
            if value:
                for cache in missed_caches:
                    cache.set(key, value)
                return value
            else:
                missed_caches.append(cache)
        return default

    def set(self, key, value, timeout=None, version=None):
        for cache in self.caches:
            cache.set(key, value, timeout=timeout, version=version)

    def add(self, key, value, timeout=None, version=None):
        for cache in self.caches:
            cache.add(key, value, timeout=timeout, version=version)

    def delete(self, key, version=None):
        for cache in self.caches:
            cache.delete(key, version=version)

    def has_key(self, key, version=None):
        has_key = False
        for cache in self.caches:
            has_key = cache.has_key(key, version=version)
            if has_key:
                return has_key
        return has_key

    def clear(self):
        for cache in self.caches:
            cache.clear()
