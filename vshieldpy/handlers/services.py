"""Operations related to services."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from ..api_defs import AutoRenew, Payment
from ..products import DedicatedServer, Hosting, Services


def _is_numeric(nums: str) -> bool:
    return nums.isnumeric()


def _is_ip(ip_addr: str) -> bool:
    return all(map(_is_numeric, ip_addr.split(sep=".")))


if TYPE_CHECKING:
    from typing import Any


def _construct_service(service) -> DedicatedServer | Hosting:
    construct: type[DedicatedServer] | type[Hosting]
    if _is_ip(service["info"]):
        construct = DedicatedServer
    else:
        construct = Hosting

    return construct(
        service["id"],
        service["info"],
        bool(service["status"]),
        datetime.fromtimestamp(service["expiration"]),
    )


def _get_list(response: list[dict[str, Any]]):
    services = Services(tuple(map(_construct_service, response)))
    return services


def _get_service(response: dict[str, Any]):
    return _construct_service(response)


def _create_task(response: dict[str, Any]) -> bool:
    return response["taskCreated"]


def _set_auto_renew(response: dict[str, Any]) -> AutoRenew:
    val = int(response["newStatus"])
    return AutoRenew(val)


def _renew(response: dict[str, Any]):
    expiration = datetime.fromtimestamp(response["newExpiration"])
    return Payment(
        response["transactionPrice"],
        response["newBalance"],
        expiration,
    )
