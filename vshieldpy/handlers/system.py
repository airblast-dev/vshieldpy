"""Operations related to system."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

import pycountry

from ..api_defs import Actions, Plans, StockStatus, Task, TaskStatus
from ..helpers import _match_product_from_id
from ..products import server

if TYPE_CHECKING:
    from typing import Any, Literal

    from ..api_defs import _SERVER_CLASSES, _SERVER_PLANS, _STATUS_CODE


def _get_list(
    response: dict[
        _SERVER_CLASSES,
        dict[str, dict[_SERVER_PLANS, dict[Literal["status"], _STATUS_CODE]]],
    ]
) -> StockStatus:
    server_stock_status: dict[
        _SERVER_CLASSES, dict[str, dict[_SERVER_PLANS, dict[Literal["status"], bool]]]
    ] = {}
    for server_type, statuses in response.items():
        server_stock_status[server_type] = {}
        for location, products in statuses.items():
            products = _match_product_from_id(products)
            server_stock_status[server_type][location] = {
                product: {"status": bool(status["status"])}
                for product, status in products.items()
            }
    return StockStatus(server_stock_status)


def _get_pending_orders(response: list[dict[str, Any]]) -> list[server.PendingServer]:
    pending_servers = []
    for order in response:
        date_paid = datetime.fromtimestamp(order["datePaid"])
        location = pycountry.countries.lookup(order["location"]).alpha_2
        pending_server = server.PendingServer(
            _id=order["id"],
            hostname=order["hostname"],
            plan=Plans(order["plan"].replace("-", "_")),
            location=location,
            date_paid=date_paid,
        )
        pending_servers.append(pending_server)
    return pending_servers


def _get_task_info(response: dict[str, Any]) -> Task:
    return Task(
        Actions(response["type"])
        if response["type"] != "shutdown"
        else Actions("stop"),
        datetime.fromtimestamp(response["dateCompleted"]),
        datetime.fromtimestamp(response["date"]),
        TaskStatus(response["status"]),
    )
