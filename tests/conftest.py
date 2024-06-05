from multiprocessing import Process

import pytest

import vshieldpy

from .requests.vs_api import app


# TODO: This always works, however a proper way to assure the server has started should be implemented.
@pytest.fixture(scope="session", autouse=True)
def test_server():
    proc = Process(target=app.run, kwargs={"host": "localhost", "port": 5000})
    proc.start()
    yield
    proc.kill()
    proc.join()


@pytest.fixture
def anyio_backend():
    return "asyncio"


client = vshieldpy.Client()
