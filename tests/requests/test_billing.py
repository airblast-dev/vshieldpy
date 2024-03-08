import pytest

from vshieldpy.api_defs.invoices import Invoice
from vshieldpy.api_defs.transactions import Transaction

from . import client

pytestmark = pytest.mark.anyio


async def test_get_balance():
    await client.fetch_balance()


async def test_get_transactions():
    transactions = await client.fetch_transactions()
    assert type(transactions) == tuple
    assert all([type(transaction) == Transaction for transaction in transactions])


async def test_get_invoices():
    invoices = await client.fetch_invoices()
    assert type(invoices) == tuple
    assert all([type(invoice) == Invoice for invoice in invoices])


async def test_get_invoice():
    invoice = await client.fetch_invoice(1)
    assert type(invoice) == Invoice
