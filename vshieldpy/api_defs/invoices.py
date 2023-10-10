"""Module for invoices and related operations."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Invoice:
    """Invoice object containing response information."""

    identifier: int
    status: bool
    amount: str
    amount_due: str
    kind: str
    service: int
    payment_method: str
    date_paid: datetime
    date: datetime
    due_date: datetime
