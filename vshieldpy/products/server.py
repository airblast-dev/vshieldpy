"""For products that classify as server."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional

from ..api_defs import AutoRenew, OperatingSystems, Plans


@dataclass(init=True, slots=True)
class Server:
    """Server object for ease of use whilst controlling a server."""

    identifier: int
    ip: str
    hostname: str
    os: OperatingSystems
    plan: Plans
    autorenew: AutoRenew
    status: bool
    node: str
    expiration: datetime
    creationdate: datetime
    password: Optional[str] = None
    _client: Any = field(init=False)


@dataclass(slots=True)
class PendingServer:
    """A server that is pending deployment.

    Provides information currently available.
    """

    def __init__(
        self, _id: int, hostname: str, plan: Plans, location: str, date_paid: datetime
    ):
        self.id = _id
        self.hostname = hostname
        self.plan = plan
        self.location = location
        self.date_paid: datetime
