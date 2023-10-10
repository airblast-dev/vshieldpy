"""Products that are referred as a service."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class DedicatedServer:
    """Dedicated server object with ease of use methods."""

    identifier: int
    ip: str
    status: bool
    expiration: datetime


@dataclass(slots=True)
class Hosting:
    """Hosting server object with ease of use methods."""

    identifier: int
    domain: str
    status: bool
    expiration: datetime
