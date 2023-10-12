"""All exceptions that vshieldpy can raise."""


class VShieldpyException(Exception):
    """Raised if there is an unkown API error returned. Also serves as a base exception.

    Can also mean format wise correct but invalid auth key was provided.
    """

    def __init__(self, error: str | None = None, api_error: str | None = None):
        super().__init__(
            error
            or f'requestStatus was returned "0". Error returned from API: "{api_error}"'
        )


class InvalidParameter(VShieldpyException):
    """Raised if an invalid parameter was provided for any function or request."""

    def __init__(self, provided_val, accepted_vals=None):
        super().__init__(f"Expected one of {accepted_vals}, found {provided_val}")


class InvalidServerId(VShieldpyException):
    """Invalid Server ID was provided.

    Raised if a provided server Id is for a for a server that isnt owned by
    the user or doesnt exist.
    """

    def __init__(self):
        super().__init__("Invalid server ID provided.")


class InvalidAuthKey(VShieldpyException):
    """Raised upon finding an invalid format (non base16) auth key."""

    def __init__(self, auth_key):
        super().__init__(
            f"Invalid auth key was provided, auth key must be a base16 string. "
            f"{auth_key} is not a valid key."
        )


class ReinstallWithoutOS(InvalidParameter):
    """Raised if a reinstall is requested without specifying an Operating system."""

    def __init__(self):
        super().__init__(
            "Attempted reinstall task without providing an Operating System."
        )
