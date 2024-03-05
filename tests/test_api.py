import os
from threading import Thread

import pytest
from vs_api import app

os.environ["VS_API_URL"] = "http://localhost:5000"
os.environ["VS_API_KEY"] = "1"

import vshieldpy


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


def test_client():
    from vshieldpy.exceptions import auth_exceptions

    # Test valid base16 auth.
    vshieldpy.Client()

    # Test invalid base16 auth.
    with pytest.raises(auth_exceptions.InvalidAuthKey):
        vshieldpy.Client("This isnt base16 lmao")


client = vshieldpy.Client()
