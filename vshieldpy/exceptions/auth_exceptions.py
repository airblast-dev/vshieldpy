"""Authentication related exceptions."""

from .base_exception import VShieldpyException


class InvalidAuthKey(VShieldpyException):
    """Raised upon finding an invalid format (non base16) auth key, or the key was not accepted by the API."""

    def __init__(self, auth_key):
        super().__init__(
            f"Invalid auth key was provided, auth key must be a base16 integer as a string. "
            f"{auth_key} is not a valid key."
        )
