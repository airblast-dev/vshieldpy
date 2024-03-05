import pytest
from test_api import client

pytestmark = pytest.mark.anyio


async def test_get_balance():
    await client.fetch_balance()


async def test_get_transactions():
    await client.fetch_transactions()


async def test_get_invoices():
    await client.fetch_invoices()


async def test_get_invoice():
    await client.fetch_invoice(1)
