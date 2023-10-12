"""For products that classify as server."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional

from ..api_defs import AutoRenew, OperatingSystems, Plans


@dataclass(slots=True)
class Servers:
    """Group of `~Server`'s.

    Contains servers and provides ease of use methods to get a  certain server.
    Such as getting server from hostname.
    """

    servers: tuple[Server]


@dataclass(init=True, slots=True)
class Server:
    """Server object for ease of use whilst controlling a server.

    Attributes:
        identifier: Identifier of the server.
        ip: IP address of the server.
        hostname: Hostname of the server.
        os: Operating system that is currently installed.
        plan: Plan of the server.
        autorenew: Current auto-renew status.
        status: If the server is running value is True and False if stopped.
        node: The node that the server is located in.
        expiration: Date of expiration.
        creation_date: Date of when the server was deployed.
        password: Password of the server.
            Only contains a password if the specifically requested with the server ID.
    """

    identifier: int
    ip: str
    hostname: str
    os: OperatingSystems
    plan: Plans
    autorenew: AutoRenew
    status: bool
    node: str
    expiration: datetime
    creation_date: datetime
    password: Optional[str] = None
    _client: Any = field(init=False)


@dataclass(slots=True)
class PendingServer:
    """A server that is pending deployment.

    Provides information currently available.

    Attributes:
        identifier: Identifier of the not yet deployed server.
        hostname: Hostname of the server.
        plan: Plan of the ordered server.
        location: Location of the server.
        date_paid: Date when the invoice for the server was paid.
    """

    identifier: int
    hostname: str
    plan: Plans
    location: str
    date_paid: datetime
