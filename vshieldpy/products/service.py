"""Products that are referred as a service."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class DedicatedServer:
    """Dedicated server object with ease of use methods.

    Attributes:
        identifier: Identifier of the dedicated server.
        ip: IP address of the dedicated server.
        status: If server is running value is True if not False.
        expiration: Date of expiration of the server.
    """

    identifier: int
    ip: str
    status: bool
    expiration: datetime


@dataclass(slots=True)
class Hosting:
    """Hosting object containing related information.
    
    Attributes:
        identifier: Identifier of the hosting.
        domain: Domain assigned to the hosting.
        status: If running value is True if not value is False.
        expiration: Date of when the hosting expires.
    """

    identifier: int
    domain: str
    status: bool
    expiration: datetime
