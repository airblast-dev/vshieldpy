"""Assortment common use handler functions."""
from __future__ import annotations

from typing import TYPE_CHECKING

import pycountry

if TYPE_CHECKING:
    from typing import Any

_PRODUCT_NAMES = {
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


def _match_product_from_id(product_ids: dict[str, Any]) -> dict[str, Any]:
    _matched: dict[str, Any] = {}
    for product_id in product_ids:
        product_name = _PRODUCT_NAMES[product_id]
        _matched[product_name] = product_ids[product_id]

    return _matched


def _location_to_codename(area: str):
    # vShields API location naming scheme is basically country/continent code for
    # single word countries/continents.
    #
    # For multi word countries alpha_2 code is used.
    if " " in area:
        return pycountry.countries.get(name=area).alpha_2
    match area.lower():
        case "africa":
            return "AF"
        case "asia":
            return "AS"
        case "europe":
            return "EU"
        case "na":
            return "NA"
        case "sa":
            return "SA"
        case "oc":
            return "OC"
        case "an":
            return "AN"
