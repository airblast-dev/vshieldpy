"""Payment related objects and functions."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(slots=True, frozen=True)
class Payment:
    """Payment information returned by the API."""

    price: str
    new_balance: str
    expiration: Optional[datetime] = None
    invoice_id: Optional[str] = None
