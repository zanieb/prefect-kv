from prefect_kv import KVStore, InvalidKVStore


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
    assert repr(store) == "KVStore('test')"


def test_store_set_and_get():
    store = KVStore(name="test")
    store.set("foo", "test")
    assert store.get("foo") == "test"


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
