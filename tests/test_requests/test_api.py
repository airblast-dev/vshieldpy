from threading import Thread

import pytest
from vs_api import app
import vshieldpy


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


def test_client():
    from vshieldpy.exceptions import auth_exceptions

    # Test valid base16 auth.
    vshieldpy.Client()

    # Test invalid base16 auth.
    with pytest.raises(auth_exceptions.InvalidAuthKey):
        vshieldpy.Client("This isnt base16 lmao")


client = vshieldpy.Client()

# TODO: Implement `system` test calls.
# This would probably better to do once a standard way to provide locations is impleneted.

# TODO: Implement testing for return type methods, and validate class properties, fields, and method based API calls.
# Validating method based API calls is low priority since it simply passes arguments to the underlying client.
# Meaning there is a very big chance type checkers will catch any mistakes, since they only contain little to no logic.
# However things like server statistic's related methods, or properties can contain complex logic, and should be tested.
