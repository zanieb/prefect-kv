from prefect.blocks.system import JSON
from prefect.utilities.asyncutils import sync_compatible
from prefect.utilities.collections import AutoEnum
from typing import Any

KV_STATE_KEY = "__prefect_kv_state__"
KV_PREFIX = "prefect-kv-"


class KVStoreState(AutoEnum):
    # This may be used in the future for some sort of locking mechanism
    READY = AutoEnum.auto()


class InvalidKVStore(Exception):
    """Your store is bad"""


class KVStore:
    def __init__(self, name: str) -> None:
        self.name = name
        self._full_name = (KV_PREFIX + name) if not name.startswith(KV_PREFIX) else name

    @property
    def full_name(self) -> str:
        return self._full_name

    async def _get_store(self) -> JSON:
        try:
            store = await JSON.load(self.full_name)
        except ValueError as exc:
            if "Unable to find" not in str(exc):
                raise  # TODO: Eek!
            store = JSON(value={KV_STATE_KEY: KVStoreState.READY})

        contents = store.value
        if not isinstance(contents, dict):
            raise InvalidKVStore(
                f"Block {self.full_name!r} is not a valid key value store."
            )
        if contents.get(KV_STATE_KEY) is None:
            raise InvalidKVStore(
                f"Block {self.full_name!r} is not a valid key value store."
            )
        return store

    @sync_compatible
    async def set(self, key: str, value: Any) -> None:
        store = await self._get_store()
        if key == KV_STATE_KEY:
            raise ValueError("You may not set the {KV_STATE_KEY!r")
        store.value[key] = value
        await store.save(self.full_name, overwrite=True)

    @sync_compatible
    async def get(self, key: str, default=None) -> Any:
        contents = await self.dict()
        return contents.get(key, default)

    @sync_compatible
    async def dict(self) -> dict:
        store = await self._get_store()
        store.value.pop(KV_STATE_KEY)
        return store.value

    def __repr__(self) -> str:
        return f"KVStore(name={self.name!r})"

    def __setitem__(self, __key: str, __value: Any) -> None:
        return self.set(__key, __value)

    def __getitem__(self, __key: str) -> None:
        contents = self.dict()
        if __key not in contents:
            raise KeyError(f"Key {__key!r} not found in store {self.full_name!r}.")

        return contents[__key]


if __name__ == "__main__":
    store = KVStore(name="demo-store")
    print(f"Created store {store!r}")

    store.set("foo", "test")
    print("Set value 'test' for key 'foo'")
    print(f"Got value {store.get('foo')!r} for key 'foo'")

    store["bar"] = "another test"
    print("Set value 'another test' for key 'bar")
    print(f"Got value {store['bar']!r} for key 'bar'")

    store["bar"] = "hello"
    print("Updated key 'bar' to 'hello'")
    print(f"Got value {store['bar']!r} for key 'bar'")

    print(f"Here's the whole thing: {store.dict()}")
