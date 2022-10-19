from prefect_kv import KVStore, InvalidKVStore
from prefect.testing.utilities import prefect_test_harness
import pytest


@pytest.fixture(autouse=True)
def isolated_database():
    with prefect_test_harness():
        yield


def test_store_name():
    store = KVStore(name="demo-store")
    assert store.name == "demo-store"


def test_store_name_full_name():
    store = KVStore(name="prefect-kv-demo-store")
    assert store.full_name == "prefect-kv-demo-store"

    store = KVStore(name="demo-store")
    assert store.full_name == "prefect-kv-demo-store"


def test_store_repr():
    store = KVStore(name="test")
    assert repr(store) == "KVStore(name='test')"


def test_store_set_and_get():
    store = KVStore(name="test")
    store.set("foo", "test")
    assert store.get("foo") == "test"


def test_store_set_and_get_new_instance():
    store1 = KVStore(name="test")
    store2 = KVStore(name="test")
    store1.set("foo", "test")
    assert store2.get("foo") == "test"
    store2.set("bar", "test")
    assert store1.get("bar") == "test"


def test_store_set_and_get_item_syntax():
    store = KVStore(name="test")
    store["foo"] = "test"
    assert store["foo"] == "test"


def test_store_get_with_default():
    store = KVStore(name="test")
    assert store.get("foo", "bar") == "bar"
    store.set("foo", "test")
    assert store.get("foo", "bar") == "test"


def test_store_dict():
    store = KVStore(name="test")
    assert store.dict() == {}
    store["a"] = 1
    store["b"] = 2
    assert store.dict() == {"a": 1, "b": 2}
