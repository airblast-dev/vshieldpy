"""Exceptions for ID related errors."""
from .base_exception import VShieldpyException


class InvalidID(VShieldpyException):
    """Base class for Invalid ID exceptions."""

    def __init__(self, msg: str | None = None):
        super().__init__(msg or "Invalid ID provided.")


class InvalidServerID(InvalidID):
    """Raised when a provided Server ID is invalid."""

    def __init__(self, server_id: str):
        super().__init__(
            f"Invalid Server ID was provided. {server_id} is not an accepted Server ID."
        )


class InvalidTaskID(InvalidID):
    """Raised when a provided Service ID is invalid."""

    def __init__(self, task_id: str):
        super().__init__(
            f"Invalid Task ID was provided. {task_id} is not an accepted Task ID."
        )


class InvalidServiceID(InvalidID):
    """Raised when a provided Server ID is invalid."""

    def __init__(self, service_id: str):
        super().__init__(
            f"Invalid Service ID was provided. {service_id} is not an accepted Service ID."
        )
