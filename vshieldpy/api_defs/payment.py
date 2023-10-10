"""Payment related objects and functions."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(slots=True, frozen=True)
class Payment:
    """Payment information returned by the API.

    Attributes:
        price: Amount that was paid.
        new_balance: Current balance of the account.
        expiration: Expiration of the invoice.
        invoice_id: The invoices identifier.
    """

    price: str
    new_balance: str
    expiration: Optional[datetime] = None
    invoice_id: Optional[str] = None
