"""General parameter exceptions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .base_exception import VShieldpyException

if TYPE_CHECKING:
    from typing import Any, Sequence


class InvalidParameter(VShieldpyException):
    """Raised if an invalid parameter was provided for a request.

    Means the API did not respond with any information about the reason of the error beyond being a parameter error.
    """

    def __init__(self, msg: str | None = None):
        super().__init__(
            msg
            or "Invalid parameter provided. Generally means an unclear reason was returned from the API."
        )


class ReinstallWithoutOS(InvalidParameter):
    """Raised if a reinstall is requested without specifying an Operating system."""

    def __init__(self):
        super().__init__(
            "Attempted reinstall task without providing an Operating System."
        )


class InvalidHostname(InvalidParameter):
    """Raised if a provided hostname contains non-ascii items, or is longer than 16 characters."""

    def __init__(self, hostname: str):
        super().__init__(
            "Invalid hostname provided. Hostname can only contain alphabetic ascii characters"
            f', and must be at most 16 characters long. Provided hostname was "{hostname}".'
        )


class InvalidDuration(InvalidParameter):
    """Raised if a non-accepted value is provided for a duration. Intended to be used as a base exception."""


class InvalidDays(InvalidParameter):
    """Raised if an order, or renewal was attempted with a non-accepted duration in days."""

    def __init__(self, provided_val: Any, expected_vals: Sequence[int] | str):
        super().__init__(
            f"Expected one of {'values in' if not isinstance(expected_vals, str) else ''} {expected_vals}. Found {provided_val}."
        )


class InvalidMonths(InvalidDuration):
    """Raised if an order, or renewal was attempted with a non-accepted duration in months."""

    def __init__(self, provided_val: Any, expected_vals: Sequence[int]):
        super().__init__(f"Expected one of {expected_vals}. Found {provided_val}.")
