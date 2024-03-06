"""UAM Status related items."""

from enum import Enum


class UAMStatus(Enum):
    """UAM status currently selected on the panel."""

    Disabled = 0
    Automatic = 1
    Forced = 2
