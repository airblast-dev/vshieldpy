"""Operations related to servers."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from ..api_defs import AutoRenew, OperatingSystems, Payment, Plans, ServerStats, Status
from ..products import Server, Servers

if TYPE_CHECKING:
    from typing import Any, Literal


def _sort_by_id(server: Server) -> int:
    return server.identifier


def _get_list(response: list[dict[str, Any]]) -> Servers:
    server_list = [_get_server(server_r) for server_r in response]
    server_list.sort(key=_sort_by_id)
    return Servers(tuple(server_list))


def _get_server(response: dict[str, Any]) -> Server:
    """Factory function for constructing Server object."""
    try:
        os = OperatingSystems(response["os"])
    except ValueError:
        os = OperatingSystems.Custom

    return Server(
        response["id"],
        response["ip"],
        response["hostname"],
        os,
        Plans(response["plan"]),
        AutoRenew(response["autorenew"]),
        Status(response["status"]),
        response["node"],
        datetime.fromtimestamp(response["expiration"]),
        datetime.fromtimestamp(response["creationdate"]),
        response.get("password"),
    )


def _get_server_stats(response) -> ServerStats:
    return ServerStats(response)


def _get_server_console(response: dict[str, Any]) -> str:
    return response["sessionUrl"]


def _create_server_task(response: dict[str, Any]) -> bool:
    return response["taskId"]


def _set_auto_renew(response: dict[str, Any]):
    status = int(response["newStatus"])
    return AutoRenew(status)


def _set_hostname(response: dict[str, Any]) -> str:
    return response["newHostname"]


def _upgrade(response: dict[str, Any]):
    return Payment(response["transactionPrice"], response["newBalance"])


def _change_ip(response: dict[str, Any]):
    return Payment(response["transactionPrice"], response["newBalance"])


def _renew(response: dict[str, Any]):
    return Payment(
        response["transactionPrice"],
        response["newBalance"],
        datetime.fromtimestamp(response["newExpiration"]),
    )


def _delete(response: dict[Literal["taskId"], int]) -> int:
    return int(response["taskId"])


def _order(response: dict[str, Any]) -> Payment:
    return Payment(
        response["transactionPrice"],
        response["newBalance"],
        None,
        str(response["generatedInvoice"]),
    )
