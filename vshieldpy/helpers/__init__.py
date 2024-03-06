"""Assortment common use handler functions."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Literal

from ..api_defs import _SERVER_PLANS, _STATUS_CODE

if TYPE_CHECKING:
    from typing import Any

_PRODUCT_NAMES: dict[str, str] = {
    "1": "VDS_1",
    "2": "VDS_2",
    "3": "VDS_3",
    "4": "VDS_PRO_BRONZE",
    "5": "VDS_PRO_SILVER",
    "6": "VDS_PRO_GOLD",
    "7": "VDS_PRO_DIAMOND",
    "8": "VDS_PRO_ENTERPRISE",
    "9": "VPS_S",
    "10": "VPS_M",
    "11": "VPS_L",
    "12": "VPS_XL",
}


def _match_product_from_id(
    product_ids: dict[_SERVER_PLANS, dict[Literal["status"], _STATUS_CODE]],
) -> dict[str, Any]:
    _matched: dict[str, Any] = {}
    for product_id in product_ids:
        product_name = _PRODUCT_NAMES[product_id]
        _matched[product_name] = product_ids[product_id]

    return _matched


FORM_PARSER = re.compile("[=&]")


def _parse_form_data(data: bytes) -> dict[str, str]:
    """Used in parsing from body contents.

    Not the greatest solution for it.
    But since it is intended to be used internaly for cleaner error handling its fine as we already know the types of outputs.
    """
    _data: list[str] = FORM_PARSER.split(data.decode())
    parsed = {}
    for name, val in zip(_data[0::2], _data[1::2]):
        parsed[name] = val
    return parsed


def hostname_is_valid(hostname: str) -> bool:
    """Check if provided hostname is valid.

    Args:
        hostname: Hostname to validate.

    Returns:
        bool: `True` if hostname is valid, and `False` if it isnt.
    If hostname is valid, returns `True`, if not False.
    """
    if hostname.isascii() and hostname.isalpha() and len(hostname) <= 16:
        return True
    return False
