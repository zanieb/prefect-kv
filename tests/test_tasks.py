from prefect import flow

from prefect_kv.tasks import (
    goodbye_prefect_kv,
    hello_prefect_kv,
)


def test_hello_prefect_kv():
    @flow
    def test_flow():
        return hello_prefect_kv()

    result = test_flow()
    assert result == "Hello, prefect-kv!"


def goodbye_hello_prefect_kv():
    @flow
    def test_flow():
        return goodbye_prefect_kv()

    result = test_flow()
    assert result == "Goodbye, prefect-kv!"
