"""For products that classify as server."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional

from ..api_defs import AutoRenew, OperatingSystems, Plans
from ..exceptions import InvalidServerId


@dataclass(slots=True)
class Servers:
    """Group of `~Server`'s.

    Contains servers and provides ease of use methods to get a certain server.
    Such as getting server from hostname.
    """

    servers: tuple[Server]
    _client: Any = field(init=False)

    def __iter__(self):
        """Yields each server that is stored."""
        yield from self.servers

    def __getitem__(self, server_id: int) -> Server:
        """Gets server with the provided ID.

        Raises:
            InvalidServerId: Raised if a server with the provided server ID cannot
            be found.
        """
        for server in self.servers:
            if server.identifier == server_id:
                return server
        raise InvalidServerId

    def get_server_from_hostname(self, hostname: str) -> list[Server]:
        """Get servers via their hostname.

        Returns:
            list[Server]: The return is a list of `~Server`'s this because it is
            possible to have different servers with the same hostname's. The list can
            be empty if no servers have the provided hostname.
        """
        return [
            server for server in self.servers if server.hostname == hostname.strip()
        ]

    def get_server_from_id(self, server_id: int) -> Optional[Server]:
        """Get server via their identifier.

        This can be considered a non exception raising alternative to
        `~Server.__getitem__`.

        Returns:
            Server: A server with the provided ID exists and is returned.

        Raises:
            InvalidServerId: A server with the provided ID was not found.
        """
        for server in self.servers:
            if server.identifier == server_id:
                return server
        return None

    async def refresh(self, keep_old_pass: bool = False) -> None:
        """Refreshes all stored servers.

        Arguments:
            keep_old_pass: If set to True, transfers passwords to new `~Servers`.
                This is done by matching the server's ID.
        """
        new_servers = await self._client.fetch_servers()
        if keep_old_pass:
            for old_server in self.servers:
                for new_server in new_servers:
                    if old_server.identifier == new_server.identifier:
                        new_server.password = old_server.password
        self.servers = new_servers


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

    async def fetch_password(self) -> str:
        """Fetches the password in case the its outdated or missing alltogether.

        Once this function is called the password can also be read from the
        `password` attribute. Calling will function will renew the password stored
        in the `password` attribute.

        Returns:
            str: The servers password.
        """
        _server = await self._client.fetch_server(self.identifier)
        self.password = _server.password
        return self.password


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
