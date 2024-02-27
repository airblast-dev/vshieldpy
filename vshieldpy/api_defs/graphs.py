"""Module for server statistics."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypedDict

    class _CpuStat(TypedDict):
        date: datetime
        cpu: int

    class _RamStat(TypedDict):
        date: datetime
        ram: int

    _NetworkStat = TypedDict(
        "_NetworkStat", {"date": datetime, "in": float, "out": float}
    )

    class _ServerGraph(TypedDict):
        cpu_last_1hr: list[_CpuStat]
        ram_last_1hr: list[_RamStat]
        network_last_1hr: list[_NetworkStat]
        cpu_last_24hrs: list[_CpuStat]
        ram_last_24hrs: list[_RamStat]
        network_last_24hrs: list[_NetworkStat]


@dataclass(slots=True)
class ServerStats:
    """Ease of use properties related to statistics."""

    raw: _ServerGraph

    @property
    def cpu_avg_last_1hr(self) -> float:
        """Average CPU load for the last hour."""
        cpu = self.raw["cpu_last_1hr"]
        return sum([stat["cpu"] for stat in cpu]) / len(cpu)

    @property
    def ram_avg_last_1hr(self) -> float:
        """Average ram usage for the last hour."""
        ram = self.raw["ram_last_1hr"]
        return sum([stat["ram"] for stat in ram]) / len(ram)

    @property
    def network_avg_last_1hr(self) -> tuple[float, float]:
        """Average network input and output for the last hour."""
        network = self.raw["network_last_1hr"]
        rx = sum([stat["in"] for stat in network]) / len(network)
        tx = sum([stat["out"] for stat in network]) / len(network)
        return rx, tx

    @property
    def cpu_avg_last_24hrs(self) -> float:
        """Average CPU load for the last 24 hours."""
        cpu = self.raw["cpu_last_24hrs"]
        return sum([stat["cpu"] for stat in cpu]) / len(cpu)

    @property
    def ram_avg_last_24hrs(self) -> float:
        """Average RAM load for the last 24 hours."""
        ram = self.raw["ram_last_24hrs"]
        return sum([stat["ram"] for stat in ram]) / len(ram)

    @property
    def network_avg_last_24hrs(self) -> tuple[float, float]:
        """Average network input and output for the last 24 hours."""
        network = self.raw["network_last_24hrs"]
        rx = sum([stat["in"] for stat in network]) / len(network)
        tx = sum([stat["out"] for stat in network]) / len(network)
        return rx, tx
