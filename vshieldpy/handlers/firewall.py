"""Handler for firewall related requests."""

from datetime import datetime
from typing import TYPE_CHECKING

from ..products import Attack, Firewall, Subdomain, Subdomains

if TYPE_CHECKING:
    from typing import Any


def _construct_subdomain(response: dict[str, Any]) -> Subdomain:
    return Subdomain(
        response["id"],
        response["info"],
        bool(response["uam"]),
        response["ratelimit"],
        response["backend"],
        response["date"],
    )


def _construct_attack(response: dict[str, Any]) -> Attack:
    return Attack(
        response["id"],
        response["averagepersec"],
        response["peak"],
        response["percentblocked"],
        bool(response["status"]),
        datetime.fromtimestamp(response["date"]),
        datetime.fromtimestamp(response["dateEnd"]),
    )


def _get_firewall(response: dict[str, Any]) -> Firewall:
    return Firewall(
        response["underAttack"],
        response["allowedReqPerSec"],
        response["blockedReqPerSec"],
        Subdomains(tuple(map(_construct_subdomain, response["subdomains"]))),
        tuple(map(_construct_attack, response["attackHistory"])),
    )
