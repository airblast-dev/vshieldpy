"""Module for renewal related data."""

from enum import Enum


class AutoRenew(Enum):
    """Auto-renew options."""

    Enable = 1
    Disable = 0
