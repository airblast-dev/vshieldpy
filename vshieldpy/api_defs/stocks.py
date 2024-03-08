"""Module for stocks and related operations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .locations import Locations
from .plans import Plans

if TYPE_CHECKING:
    from typing import Literal

    from .type_defs import _SERVER_CLASSES, _SERVER_PLANS


class StockStatus:
    """StockStatus for ease of use for per plan lookups."""

    __slots__ = "_stocks"

    def __init__(
        self,
        result: dict[
            _SERVER_CLASSES,
            dict[str, dict[_SERVER_PLANS, dict[Literal["status"], bool]]],
        ],
    ):
        self._stocks = [
            _Stock(_class, Plans[plan], Locations(location), status["status"])
            for _class, locations in result.items()
            for location, plans in locations.items()
            for plan, status in plans.items()
        ]

    def check_stock(self, plan: Plans, location: Locations) -> bool:
        """Check stock for provided plan and country code."""
        for stock in self._stocks:
            if location == stock.location and plan == stock.plan:
                return stock.status
        return False

    def get_locations(
        self, plan: Plans, only_in_stocks: bool = False
    ) -> tuple[Locations, ...]:
        """Get locations for the provided plan."""
        locations = list()
        for stock in self._stocks:
            if stock.plan != plan or stock.location in locations:
                continue

            if not only_in_stocks:
                locations.append(stock.location)
            elif stock.status:
                locations.append(stock.location)
            continue
        return tuple(locations)


@dataclass
class _Stock:
    def __init__(
        self, _class: _SERVER_CLASSES, plan: Plans, location: Locations, status: bool
    ):
        self._class = _class
        self.plan = plan
        self.location = location
        self.status = status
