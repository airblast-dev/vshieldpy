"""Handler for firewall related requests."""

from datetime import datetime

from ..api_defs import UAMStatus
from ..products import Attack, Firewall, Subdomain, Subdomains


def _construct_subdomain(response: dict) -> Subdomain:
    return Subdomain(
        response["id"],
        response["info"],
        bool(response["uam"]),
        response["ratelimit"],
        response["backend"],
        response["date"],
    )


def _construct_attack(response: dict) -> Attack:
    return Attack(
        response["id"],
        response["averagepersec"],
        response["peak"],
        response["percentblocked"],
        UAMStatus(response["status"]),
        datetime.fromtimestamp(response["date"]),
        datetime.fromtimestamp(response["dateEnd"]),
    )


def _get_firewall(response: dict) -> Firewall:
    return Firewall(
        response["underAttack"],
        response["allowedReqPerSec"],
        response["blockedReqPerSec"],
        Subdomains(tuple(map(_construct_subdomain, response["subdomains"]))),
        tuple(map(_construct_attack, response["attackHistory"])),
    )
