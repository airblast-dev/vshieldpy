from threading import Thread

import pytest

import vshieldpy

from .requests.vs_api import app


# FIX: This almost always works, however a proper way to assure the server has started should be implemented.
@pytest.fixture(scope="session", autouse=True)
def test_server():
    thread = Thread(
        target=app.run,
        daemon=True,
        kwargs={
            "host": "localhost",
            "port": 5000,
        },
    )
    thread.start()


client = vshieldpy.Client()
