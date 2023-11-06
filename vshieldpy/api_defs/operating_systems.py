"""Module for operating systems and related operations."""

from enum import Enum


class OperatingSystems(Enum):
    """Operating systems that can be installed on server's and dedicated server's."""

    WindowsServer22 = "winserv22"
    WindowsServer19 = "winserv19"
    Debian10 = "debian10"
    Ubuntu20 = "ubuntu20"
    Centos9 = "centos9"
    Custom = ""
