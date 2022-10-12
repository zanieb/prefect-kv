from . import _version

__version__ = _version.get_versions()["version"]

from ._backend import KVStore as KVStore, InvalidKVStore as InvalidKVStore

