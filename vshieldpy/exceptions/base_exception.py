"""Base exception for vshieldpy."""


class VShieldpyException(Exception):
    """Raised if there is an unkown API error returned. Also serves as a base exception."""

    def __init__(self, error: str | None = None, api_error: str | None = None):
        super().__init__(
            error
            or f'requestStatus was returned "0". Error returned from API: "{api_error}"'
        )
