import pytest
from prefect.testing.utilities import prefect_test_harness


@pytest.fixture(autouse=True)
def isolated_database():
    with prefect_test_harness():
        yield
