"""Status codes for vShield services."""

from enum import Enum


class Status(Enum):
    """All of statuses are quite self explanitory.

    However its worth noting that "Installing" is for an initial install of an OS on a server.
    """

    Stopped = 0
    Running = 1
    Suspended = 2
    Installing = 3
    Reinstalling = 4
