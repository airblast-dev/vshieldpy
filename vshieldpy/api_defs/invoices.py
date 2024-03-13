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
        service: Service ID. This includes Server ID's and services. Can be None if a server hasnt been deployed yet.
        payment_method: Method of payment.
        date_paid: Date the invoice was paid. Can also be `None` if the invoice hasn't been paid yet.
        date: The date that the invoice was created.
        due_date: Due date for the invoice.
    """

    identifier: int
    status: bool
    amount: str
    amount_due: str
    kind: str
    service: int | None
    payment_method: str
    date_paid: datetime | None
    date: datetime
    due_date: datetime
