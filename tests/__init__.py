from mock import Mock
from django.core.cache import get_cache

BackendOne = Mock(get_cache('django.core.cache.backends.dummy.DummyCache'))
BackendTwo = Mock(get_cache('django.core.cache.backends.dummy.DummyCache'))
