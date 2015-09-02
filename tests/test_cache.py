from combocache import ComboCache
from mock import Mock
import pytest

CACHE_BACKENDS = ['tests.BackendOne', 'tests.BackendTwo']

PARAMS = {
    'CACHES': CACHE_BACKENDS
}

TEST_KEY = 'mykey'
TEST_VALUE = 'myvalue'


def test_cache_get():
    """
    Make sure only the first cache backend's `get` method is called
    """
    cc = ComboCache(None, PARAMS)
    assert cc.get(TEST_KEY)
    assert cc.caches[0].get.call_count == 1
    assert cc.caches[1].get.call_count == 0


def test_cache_set():
    """
    Make sure both cache backend's `set` method is called with correct values
    """
    cc = ComboCache(None, PARAMS)
    cc.set(TEST_KEY, TEST_VALUE)
    assert cc.caches[0].set.call_count == 1
    assert cc.caches[1].set.call_count == 1
    cc.caches[0].set.assert_called_with(
        TEST_KEY, TEST_VALUE, version=None, timeout=None)
    cc.caches[1].set.assert_called_with(
        TEST_KEY, TEST_VALUE, version=None, timeout=None)


def test_cache_add():
    """
    Make sure both cache backend's `add` method is called with correct values
    """
    cc = ComboCache(None, PARAMS)
    cc.add(TEST_KEY, TEST_VALUE)
    assert cc.caches[0].add.call_count == 1
    assert cc.caches[1].add.call_count == 1
    cc.caches[0].add.assert_called_with(
        TEST_KEY, TEST_VALUE, version=None, timeout=None)
    cc.caches[1].add.assert_called_with(
        TEST_KEY, TEST_VALUE, version=None, timeout=None)


def test_cache_delete():
    """
    Make sure both backend's `delete` method is called.
    """
    cc = ComboCache(None, PARAMS)
    cc.delete(TEST_KEY)
    assert cc.caches[0].delete.call_count == 1
    assert cc.caches[1].delete.call_count == 1
    cc.caches[0].delete.assert_called_with(
        TEST_KEY, version=None)
    cc.caches[1].delete.assert_called_with(
        TEST_KEY, version=None)


def test_cache_has_key():
    """
    Make sure both backend's `has_key` method is called.
    """
    cc = ComboCache(None, PARAMS)
    cc.has_key(TEST_KEY)
    assert cc.caches[0].has_key.call_count == 1
    assert cc.caches[1].has_key.call_count == 0
    cc.caches[0].has_key.assert_called_with(
        TEST_KEY, version=None)


def test_cache_clear():
    """
    Make sure both backend's `clear` method is called.
    """
    cc = ComboCache(None, PARAMS)
    cc.clear()
    assert cc.caches[0].clear.call_count == 1
    assert cc.caches[1].clear.call_count == 1


def test_cache_get_fallback():
    """
    If first cache backend returns None, fallback to the second
    """
    cc = ComboCache(None, PARAMS)
    cc.caches[0].get = Mock(return_value=None)
    assert cc.get(TEST_KEY)
    assert cc.caches[0].get.call_count == 1
    assert cc.caches[1].get.call_count == 1
    assert cc.caches[0].set.call_count == 2


def test_backends_required():
    """
    Raise exception if no backends provideds
    """
    with pytest.raises(Exception):
        ComboCache(None, {'CACHES': []})


def test_likes_combos():
    assert True
