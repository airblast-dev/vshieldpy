"""Client module for async requests to the vShield API."""

from __future__ import annotations

from typing import TYPE_CHECKING

from httpx import AsyncClient, Request

from vshieldpy.api_defs.graphs import ServerStats
from vshieldpy.api_defs.invoices import Invoice
from vshieldpy.api_defs.locations import Locations
from vshieldpy.api_defs.payment import Payment
from vshieldpy.api_defs.stocks import StockStatus
from vshieldpy.api_defs.tasks import Task
from vshieldpy.api_defs.transactions import Transaction
from vshieldpy.products.firewall import Firewall
from vshieldpy.products.server import PendingServer, Server, Servers
from vshieldpy.products.service import DedicatedServer, Hosting, Services

from .api_defs import (
    OperatingSystems,
    ServerActions,
    ServiceActions,
    _BillingRequests,
    _FirewallRequests,
    _ServerRequests,
    _ServiceRequests,
    _SystemRequests,
)
from .auth import _VShieldAuth
from .exceptions import (
    auth_exceptions,
    base_exception,
    id_exceptions,
    parameter_exceptions,
)
from .handlers import billing, firewall, servers, services, system
from .helpers import _parse_form_data, hostname_is_valid

if TYPE_CHECKING:
    from typing import Literal, Optional

    from .api_defs import AutoRenew, Plans


class Client:
    """Asynchronous client for sending requests to the vShield API.

    The naming convention for methods is similiar to a discord.py Client.
    Function names starting with fetch, send async requests and function names starting
    with get perform cache lookups. Any extra keyword arguments are passed to an `httpx
    AsyncClient <https://www.python-httpx.org/api/#asyncclient>`_.
    """

    __slots__ = ("_auth_key", "_session", "_balance", "_servers")

    # All Request constructing is done in public methods then passed to Client._request.
    def __init__(self, auth_key: str | None = None, **kwargs):
        if auth_key is None:
            import os

            auth_key = os.environ["VS_API_KEY"]

        self.auth_key = auth_key
        session = AsyncClient(auth=_VShieldAuth(auth_key), http2=True, **kwargs)
        self._session = session

    @property
    def auth_key(self) -> str:
        """Currently set authentication key."""
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        try:
            int(auth_key, base=16)
        except ValueError:
            raise auth_exceptions.InvalidAuthKey(auth_key)
        self._auth_key = auth_key

    async def _request(self, req: Request):
        response = (await self._session.send(req)).json()
        if response["requestStatus"] == 0:
            form_data = _parse_form_data(req.content)
            _id = req.url.path.split("/")[-1]
            # This isnt an elegant way to parse the ID.
            # But I also dont see much of an elegant way to do so since its just an item on path.
            match response["result"]["error"]:
                case "You are not authenticated.":
                    raise auth_exceptions.InvalidAuthKey(self.auth_key)
                case "Invalid server.":
                    raise id_exceptions.InvalidServerID(_id)
                case "Invalid service.":
                    raise id_exceptions.InvalidServiceID(_id)
                case "Invalid task Id.":
                    raise id_exceptions.InvalidTaskID(_id)
                case "Invalid hostname.":
                    raise parameter_exceptions.InvalidHostname(form_data["hostname"])
                case "Invalid order parameter(s).":
                    raise parameter_exceptions.InvalidParameter()
                case _:
                    raise base_exception.VShieldpyException(response["result"]["error"])

        return response["result"]

    async def fetch_plans(self) -> StockStatus:
        """Fetch available plans with their stock status.

        Returns:
            StockStatus:
                Current stock status of all plans.
        """
        method, url = _SystemRequests.GET_PLANS
        req = Request(method, url)
        response = await self._request(req)
        return system._get_list(response)

    async def fetch_pending_orders(self) -> list[PendingServer]:
        """Fetch currently pending orders.

        Returns:
            list[PendingServer]:
                List of servers that are currently pending deployment.
        """
        method, url = _SystemRequests.GET_PENDING_ORDERS
        req = Request(method, url)
        response = await self._request(req)
        return system._get_pending_orders(response)

    async def fetch_task_info(self, task_id: int) -> Task:
        """Fetch task information.

        Raises:
            InvalidTaskID: If the task ID provided was not valid.

        Returns:
            Task:
                Task with the ID that was provided.
        """
        method, url = _SystemRequests.GET_TASK_INFO
        url = url.join(str(task_id))
        req = Request(method, url)
        response = await self._request(req)
        return system._get_task_info(response)

    async def fetch_services(self) -> Services:
        """Fetchs all currently active services.

        Returns:
            tuple[DedicatedServer | Hosting, ...]:
                All currently active services.
        """
        method, url = _ServiceRequests.GET_LIST
        req = Request(method, url)
        response = await self._request(req)
        return services._get_list(response)

    async def fetch_service(self, service_id: int) -> Hosting | DedicatedServer:
        """Fetch a single service.

        Raises:
            InvalidServiceID: An invalid service ID was provided.
        """
        method, url = _ServiceRequests.GET_INFO
        url = url.join(str(service_id))
        req = Request(method, url)
        response = await self._request(req)
        return services._get_service(response)

    async def create_service_task(
        self,
        service_id: int,
        task: ServiceActions,
        os: Optional[OperatingSystems] = None,
    ) -> bool:
        """Create a task on a dedicated server.

        Should not be used on hosting plans.

        Args:
            service_id (int): Service ID of the service to perform the task on.
            task (ServiceActions): Task to be performed on the service.
            os (Optional[OperatingSystems], optional):
                Should only be provided if the task is a reinstall. Defaults to None.

        Raises:
            ReinstallWithoutOS:
                Attempted reinstall without providing an operating system.
            InvalidServiceID: An invalid service ID was provided.

        Returns:
            bool: If the task was created successfuly returns True.
        """
        if task == ServiceActions.Reinstall and not os:
            raise parameter_exceptions.ReinstallWithoutOS()
        method, url = _ServiceRequests.CREATE_TASK
        url = url.join(str(service_id))

        data = {
            "action": task.value,
        }
        if isinstance(os, OperatingSystems):
            data["os"] = os.value

        req = Request(method, url, data=data)
        response = await self._request(req)
        return services._create_task(response)

    async def set_service_auto_renew(
        self, service_id: int, auto_renew: AutoRenew
    ) -> AutoRenew:
        """Set the new auto-renew status for a service.

        Args:
            service_id: Service ID of the service to perform the task on.
            auto_renew: An auto-renew status. Providing `True` enables auto-renewal.

        Raises:
            InvalidServiceID: An invalid service ID was provided.

        Returns:
            AutoRenew:
                The new auto-renew status.
        """
        method, url = _ServiceRequests.SET_AUTO_RENEW
        url = url.join(str(service_id))
        data = {"status": auto_renew.value}
        req = Request(method, url, data=data)
        response = await self._request(req)
        return services._set_auto_renew(response)

    async def renew_service(self, service_id: int, months: Literal[1, 3, 6]) -> Payment:
        """Renew a specific service.

        Args:
            service_id (int): Service ID of the service to perform the task on.
            months (Literal[1, 3, 6]): Number of months to renew the server.

        Raises:
            InvalidMonths: Raised if the provided months argument is not accepted.
            InvalidServiceID: An invalid service ID was provided.

        Returns:
            Payment: The payment information returned by the API.
        """
        accepted_months = (1, 3, 6)
        if months not in accepted_months:
            raise parameter_exceptions.InvalidMonths(months, accepted_months)
        method, url = _ServiceRequests.RENEW_SERVICE

        data = {"time": months}
        url = url.join(str(service_id))
        req = Request(method, url, data=data)
        response = await self._request(req)
        return services._renew(response)

    async def fetch_servers(self) -> Servers:
        """Fetch all servers.

        Servers returned will not have password information.

        Returns:
            Servers:
                All of the servers found. Servers returned will not contain a password.
        """
        method, url = _ServerRequests.GET_LIST
        req = Request(method, url)
        response = await self._request(req)
        _servers = servers._get_list(response)
        _servers._write_clients(self)
        return _servers

    async def fetch_server(self, server_id: int) -> Server:
        """Fetch a single server.

        Returned Server will have password information.

        Args:
            server_id: Server ID of the Server to lookup information.

        Raises:
            InvalidServerID: An invalid server ID was provided.

        Returns:
            Server:
                Server object containing full information on a server.
                Including password information.
        """
        method, url = _ServerRequests.GET_INFO
        url = url.join(str(server_id))
        req = Request(method, url)
        response = await self._request(req)
        server = servers._get_server(response)
        server._client = self
        return server

    async def fetch_server_stats(self, server_id: int) -> ServerStats:
        """Fetch server stats.

        Args:
            server_id: Server ID of the server to get the statistics for.

        Raises:
            InvalidServerID: An invalid server ID was provided.

        Returns:
            ServerStats: Contains stats for the server.
        """
        method, url = _ServerRequests.GET_GRAPHS
        url = url.join(str(server_id))
        req = Request(method, url)
        response = await self._request(req)
        return servers._get_server_stats(response)

    async def fetch_server_console(self, server_id: int) -> str:
        """Fetch url for console connection.

        Args:
            server_id: Server ID of the server to get a console connection URL for.

        Raises:
            InvalidServerID: An invalid server ID was provided.

        Returns:
            str: URL for the console session.
        """
        method, url = _ServerRequests.GET_CONSOLE
        url = url.join(str(server_id))
        req = Request(method, url)
        response = await self._request(req)
        return servers._get_server_console(response)

    async def create_server_task(
        self, server_id: int, task: ServerActions, os: Optional[OperatingSystems] = None
    ) -> int:
        """Starts a task execution for corresponding server for the ID.

        Args:
            server_id: Server ID for the server to start the ask on.
            task: Task to be run on the server.
            os:
                Choice of operating system.
                Required if the task to be performed is a reinstall.

        Raises:
            InvalidServerID: An invalid server ID was provided.
            ReinstallWithoutOS:
                A reinstall task was started without providing an operating system.

        Returns:
            int: The task ID for the task that was created.
        """
        method, url = _ServerRequests.CREATE_TASK
        url = url.join(str(server_id))
        if task == ServerActions.Reinstall and not os:
            raise parameter_exceptions.ReinstallWithoutOS()
        data = {"action": task.value}
        if isinstance(os, OperatingSystems):
            data["os"] = os.value

        req = Request(method, url, data=data)
        response = await self._request(req)
        return servers._create_server_task(response)

    async def set_server_auto_renew(
        self, server_id: int, auto_renew: AutoRenew
    ) -> AutoRenew:
        """Set the server's auto-renew status.

        Args:
            server_id: Server ID of the server to set the auto-renew status to.
            auto_renew: The new auto-renew status.

        Raises:
            InvalidServerID: An invalid server ID was provided.

        Returns:
            AutoRenew: The new auto-renew status.
        """
        method, url = _ServerRequests.SET_AUTO_RENEW
        url = url.join(str(server_id))
        data = {"status": auto_renew.value}
        req = Request(method, url, data=data)
        response = await self._request(req)
        return servers._set_auto_renew(response)

    async def set_server_hostname(self, server_id: int, hostname: str):
        """Set the server's new hostname.

        Raises:
            InvalidServerID: An invalid server ID was provided.
            InvalidHostname: An invalid hostname was provided.
        """
        if not hostname_is_valid(hostname):
            raise parameter_exceptions.InvalidHostname(
                "Hostname can only contain alphabetic characters."
            )
        method, url = _ServerRequests.SET_HOSTNAME
        url = url.join(str(server_id))
        data = {"hostname": hostname}
        req = Request(method, url, data=data)
        response = await self._request(req)
        return servers._set_hostname(response)

    async def upgrade_server(self, server_id: int, upgrade: Plans) -> Payment:
        """Upgrade the server to a higher tier.

        Provided upgrade plan must be in the same class and a higher tier than what
        the servers current plan is.

        Raises:
            InvalidServerID: An invalid server ID was provided.
            InvalidParameter: A lower tier plan was provided than the server's current plan, or attempted to upgrade across different plans.
                Such as a upgrading a VDS-PRO to a VPS.

        Returns:
            Payment: Only contains the price, and the new balance.
        """
        method, url = _ServerRequests.UPGRADE_SERVER
        url = url.join(str(server_id))
        data = {"plan": str(upgrade.value)}
        req = Request(method, url, data=data)
        response = await self._request(req)
        return servers._upgrade(response)

    async def change_server_ip(self, server_id: int) -> Payment:
        """Change the server's IP.

        Raises:
            InvalidServerID: An invalid server ID was provided.

        Returns:
            Payment: Only contains the price, and new_balance.
        """
        method, url = _ServerRequests.CHANGE_IP
        url = url.join(str(server_id))
        req = Request(method, url)
        response = await self._request(req)
        return servers._change_ip(response)

    async def renew_server(self, server_id: int, days: int) -> Payment:
        """Renew the server.

        Args:
            server_id:
                Server ID for the corresponding server.
            days:
                Value must not be less than 1 and more than 365.

        Returns:
            Payment: Contains the transaction price, new balance, and the new expiration date of the server.
        """
        if not 1 <= days <= 365:
            raise parameter_exceptions.InvalidDays(days, "(1 - 365)")

        data = {"time": days}
        method, url = _ServerRequests.RENEW_SERVER
        url = url.join(str(server_id))
        req = Request(method, url, data=data)
        response = await self._request(req)
        return servers._renew(response)

    async def delete_server(self, server_id: int) -> int:
        """Deletes the server with the specified server_id.

        There is no way to reverse this. This should be called with caution.

        Args:
            server_id:
                Server ID for the corresponding server.

        Raises:
            InvalidServerID: An invalid server ID was provided.

        Returns:
            int: The task ID for the server deletion task.
        """
        method, url = _ServerRequests.DELETE_SERVER
        url = url.join(str(server_id))
        req = Request(method, url)
        response = await self._request(req)
        return servers._delete(response)

    async def order_server(
        self,
        plan: Plans,
        location: Locations,
        hostname: str,
        os: OperatingSystems,
        days: int,
    ) -> Payment:
        """Place an order for a new server.

        The server can be retrieved via
        :func:`~Client.fetch_servers`, :func:`~Client.fetch_server` or
        :func:`~Client.fetch_pending_orders` if the order is pending.

        Args:
            plan:
                The plan to be ordered.
            location:
                The location of the order.
                Valid locations of a plan can be retreived via :class:`~StockStatus`.
            hostname:
                The hostname of the new server.
                Symbols are not allowed in the provided string.
            os:
                Operating system to be installed on the server.
                If a reinstall is to be performed,
                an operating system from :class:`~OperatingSystems` must be provided.
            days:
                Value must not be less than 1 or more than 365.

        Raises:
            InvalidHostname:
                An invalid hostname was provided.
            InvalidDays:
                An invalid day count was provided.
            ReinstallWithoutOS:
                A reinstallation task was started without providing :class:`~OperatingSystems`
            InvalidParameter:
                Order parameters are incompatible.
                In particular means that the client side couldnt find any issues, and the API responded with no information.
                Often raised if a :class:`~Plans` is not sold in the provided location argument.

        Returns:
            Payment: Contains the transaction price, new balance, and the ID for the generated invoice.


        """
        if not 1 <= days <= 365:
            raise parameter_exceptions.InvalidDays(
                days, "between 1, and 365 inclusive."
            )

        if not hostname_is_valid(hostname):
            raise parameter_exceptions.InvalidHostname(
                "Hostname can only contain alphabetic characters and can be 16 characters in length."
            )

        # NOTE: I don't think making the location lower case is needed.
        # However accepted parameters on the API documentation show them as lowercase.
        # So... just to be on the safe side.
        data = {
            "location": location.value.lower(),
            "hostname": hostname,
            "os": os.value,
            "time": days,
            "plan": plan.value,
        }

        method, url = _ServerRequests.ORDER_SERVER
        req = Request(method, url, data=data)
        response = await self._request(req)
        return servers._order(response)

    async def fetch_balance(self) -> float:
        """Fetch the accounts current balance."""
        method, url = _BillingRequests.GET_BALANCE
        req = Request(method, url)
        response = await self._request(req)
        return billing._get_balance(response)

    async def fetch_transactions(self) -> tuple[Transaction, ...]:
        """Fetch list of transactions."""
        method, url = _BillingRequests.GET_TRANSACTIONS
        req = Request(method, url)
        response = await self._request(req)
        return billing._get_transactions(response)

    async def fetch_invoices(self) -> tuple[Invoice, ...]:
        """Fetch list of invoices."""
        method, url = _BillingRequests.GET_INVOICES
        req = Request(method, url)
        response = await self._request(req)
        return billing._get_invoices(response)

    async def fetch_invoice(self, invoice_id: int) -> Invoice:
        """Fetch a specific invoice.

        Args:
            invoice_id: Invoice ID to fetch information from.

        Returns:
            Invoice: Invoice object containing invoice information.
        """
        method, url = _BillingRequests.GET_INVOICE_INFO
        url = url.join(str(invoice_id))
        req = Request(method, url)
        response = await self._request(req)
        return billing._get_invoice(response)

    async def fetch_firewall(self, service_id: int) -> Firewall:
        """Fetch a specific firewall.

        Args:
            service_id: Service ID of the firewall.

        Returns:
            Firewall: Firewall object containing recent attacks, subdomains and etc.
        """
        method, url = _FirewallRequests.GET_INFO
        url = url.join(str(service_id))
        req = Request(method, url)
        response = await self._request(req)
        return firewall._get_firewall(response)
