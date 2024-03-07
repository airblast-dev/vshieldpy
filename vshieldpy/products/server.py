"""For products that classify as server."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional

from ..api_defs import AutoRenew, Locations, OperatingSystems, Plans, Status


@dataclass(slots=True)
class Servers:
    """Group of :class:`~Server`'s.

    Contains servers and provides ease of use methods to get a certain server.
    Such as getting server from hostname.

    Attributes:
        servers: Servers ordered by their identifier.
    """

    servers: tuple[Server, ...]
    _client: Any = field(init=False)

    def _write_clients(self, client):
        """Add client to all :class:`Server`'s."""
        self._client = client
        for server in self.servers:
            server._client = self._client

    def __iter__(self):
        """Yields each server that is stored."""
        yield from self.servers

    def __getitem__(self, index: int) -> Server:
        """Gets the N'th server."""
        return self.servers[index]

    def __len__(self) -> int:
        """Number of currently stored servers."""
        return len(self.servers)

    def get_server_from_hostname(self, hostname: str) -> list[Server]:
        """Get servers via their hostname.

        Returns:
            list[Server]: The return is a list of :class:`~Server`'s this because it is
            possible to have different servers with the same hostname's. The list can
            be empty if no servers have the provided hostname.
        """
        return [
            server for server in self.servers if server.hostname == hostname.strip()
        ]

    def get_server_from_id(self, server_id: int) -> Optional[Server]:
        """Get server via their identifier.

        Returns:
            Server | None: If a server with the provided ID exists it is returned.
        """
        for server in self.servers:
            if server.identifier == server_id:
                return server
        return None

    async def refresh(self, keep_old_pass: bool = False) -> None:
        """Refreshes all stored servers.

        Arguments:
            keep_old_pass: If set to True, transfers passwords to new :class:`~Servers`.
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
    status: Status
    node: str
    expiration: datetime
    creation_date: datetime
    password: Optional[str] = None
    _client: Any = field(init=False)

    async def refresh(self) -> None:
        """Refreshes all information of the server.

        This will also fetch the current password for the server.

        Raises:
            InvalidServerId: Can be raised if server was deleted or expired.
        """
        server = await self._client.fetch_server(self.identifier)
        for var_name in self.__slots__:
            setattr(self, var_name, getattr(server, var_name))


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
    location: Locations
    date_paid: datetime
