"""Types for simplified annotations.

Nothing from this module should be directly imported as they are only for annotations.
"""

from typing import Literal

_SERVER_CLASSES = Literal["VDS", "VDSPRO", "VPS"]
_SERVER_PLANS = Literal[
    "VDS1",
    "VDS2",
    "VDS3",
    "VDS_PRO_Bronze",
    "VDS_PRO_Silver",
    "VDS_PRO_Gold",
    "VDS_PRO_Diamond",
    "VDS_PRO_Enterprise",
    "VPS_S",
    "VPS_M",
    "VPS_L",
    "VPS_XL",
]
_STATUS_CODE = Literal[0, 1, 2]
_SERVER_TASKS = Literal["start"]
