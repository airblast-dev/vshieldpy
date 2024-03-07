"""Firewall module for the firewall and its sub types."""

from dataclasses import dataclass
from datetime import datetime

from vshieldpy.api_defs.uam_status import UAMStatus


@dataclass(slots=True)
class Attack:
    """Old attack containing information about the attack.

    Attributes:
        identifier: Identifier of the attack.
        average_per_second: Average requests received per second.
        peak: Peak requests per second.
        percent_blocked: Percentage of the blocked requests.
        status: # TODO
        date: Start date of the attack.
        end_date: End date of the attack.
    """

    identifier: int
    average_per_second: int
    peak: int
    percent_blocked: int
    status: UAMStatus
    date: datetime
    end_date: datetime


@dataclass(slots=True)
class Subdomain:
    """Subdomain and its current status.

    Attributes:
        identifier: Identifier of the Subdomain.
        subdomain: Subdomain URI value.
        uam: Selected UAM mode.
        rate_limit: Allowed maximum requests coming from a single user.
        backend: IP address of the backend.
        date: Date of when the subdomain was created/added.
    """

    identifier: int
    subdomain: str
    uam: bool
    rate_limit: int
    backend: str
    date: datetime


@dataclass(slots=True)
class Subdomains:
    """Subdomains object prividing practical methods for lookups."""

    subdomains: tuple[Subdomain, ...]

    def __init__(self, subdomains: tuple[Subdomain, ...]):
        self.subdomains = subdomains

    def __iter__(self):
        """Yields contained :class:`~Subdomain`'s."""
        yield from self.subdomains

    def __getitem__(self, subdomain_uri: str) -> Subdomain:
        """Get :class:`~Subdomain` via the subdomain."""
        subdomain_uri = subdomain_uri.strip()
        for subdomain in self.subdomains:
            if subdomain.subdomain == subdomain_uri:
                return subdomain
        raise KeyError

    def subdomains_as_str(self) -> list[str]:
        """List of subdomains as strings."""
        return [subdomain.subdomain for subdomain in self.subdomains]


@dataclass(slots=True)
class Firewall:
    """Firewall object containing firewall stats.

    Contains subdomain's along with old and new attack statuses.

    Attributes:
        is_under_attack: True if currently under attack and False if it isnt.
        allowed_req_per_sec: Requests that passed the firewall.
            This is the total number of accepted requests containing good
            (and possibly bad) requests.
        blocked_req_per_sec: Blocked requests per second.
        subdomains: Subdomains container for all subdomains.
        history: Old attacks that were performed on the domain.
    """

    is_under_attack: bool
    allowed_req_per_sec: int
    blocked_req_per_sec: int
    subdomains: Subdomains
    history: tuple[Attack, ...]
