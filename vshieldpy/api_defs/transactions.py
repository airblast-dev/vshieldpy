"""Module for transaction related operations."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Transaction:
    """A transaction object containing information about a transaction."""

    identifier: int
    amount: str
    invoice_id: int
    kind: str
    payment_method: str
    date: datetime
