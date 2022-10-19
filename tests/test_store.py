import runpy

import pytest
from prefect.blocks.system import JSON

from prefect_kv import InvalidKVStore, KVStore
from prefect_kv._backend import KV_PREFIX


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


def test_store_existing_invalid_block_not_a_dictionary():
    JSON(value="foo").save(KV_PREFIX + "test")
    store = KVStore(name="test")
    with pytest.raises(InvalidKVStore):
        store.get("test")


def test_store_existing_invalid_block_not_a_store():
    JSON(value={}).save(KV_PREFIX + "test")
    store = KVStore(name="test")
    with pytest.raises(InvalidKVStore):
        store.get("test")
    with pytest.raises(InvalidKVStore):
        store.set("foo", "bar")


def test_backend_demo():
    # Ignore the re-import warning
    with pytest.warns(
        RuntimeWarning,
        match="'prefect_kv._backend' found in sys.modules after import of package",
    ):
        runpy.run_module("prefect_kv._backend", run_name="__main__")
