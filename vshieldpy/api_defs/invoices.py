"""Module for invoices and related operations."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Invoice:
    """Invoice object containing response information.

    Attributes:
        identifier: Invoice ID
        status: Status of the invoice True if paid and False if unpaid.
        amount: Amount paid in USD.
        amount_due: Remaining amount to be paid.
        kind: Type of the invoice.
        service: Service value.
        payment_method: Method of payment.
        date_paid: Date the invoice was paid.
        date: Invoice creation date.
        due_date: Due date for the invoice.
    """

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
