import pytest

import vshieldpy


def test_client():
    from vshieldpy.exceptions import auth_exceptions

    # Test valid base16 auth.
    vshieldpy.Client()

    # Test invalid base16 auth.
    with pytest.raises(auth_exceptions.InvalidAuthKey):
        vshieldpy.Client("This isnt base16 lmao")
