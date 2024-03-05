"""Billing related operations. Mainly for invoices and transactions."""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from ..api_defs import Invoice, Transaction

if TYPE_CHECKING:
    from typing import Any, Literal


def _create_transaction(transaction: dict[str, Any]):
    return Transaction(
        transaction["id"],
        str(transaction["amount"]),
        transaction["invoice"],
        transaction["type"],
        transaction["paymentmethod"],
        datetime.fromtimestamp(transaction["date"]),
    )


def _get_invoice(invoice: dict[str, Any]):
    return Invoice(
        invoice["id"],
        bool(invoice["status"]),
        str(invoice["amount"]),
        str(invoice["amountdue"]),
        invoice["type"],
        invoice["service"],
        invoice["paymentmethod"],
        (
            datetime.fromtimestamp(invoice["datepaid"])
            if invoice["datepaid"] is not None
            else None
        ),
        datetime.fromtimestamp(invoice["date"]),
        datetime.fromtimestamp(invoice["duedate"]),
    )


def _get_balance(response: dict[Literal["userBalance"], float]) -> float:
    return float(response["userBalance"])


def _get_transactions(transactions: list[dict[str, Any]]):
    return tuple(map(_create_transaction, transactions))


def _get_invoices(invoices: list[dict[str, Any]]):
    return tuple(map(_get_invoice, invoices))
