"""Module for server plans that vShield offers."""

from enum import Enum


class Plans(Enum):
    """Server plans that vShield offers."""

    VDS_1 = 1
    VDS_2 = 2
    VDS_3 = 3
    VDS_PRO_BRONZE = 4
    VDS_PRO_SILVER = 5
    VDS_PRO_GOLD = 6
    VDS_PRO_DIAMOND = 7
    VDS_PRO_ENTERPRISE = 8
    VPS_S = 9
    VPS_M = 10
    VPS_L = 11
    VPS_XL = 12
