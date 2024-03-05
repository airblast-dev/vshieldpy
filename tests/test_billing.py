import os
import pytest



os.environ["VS_API_URL"] = "https://localhost:5000"

from vshieldpy.client import Client

pytestmark = pytest.mark.anyio

client = Client("1")


async def test_get_balance():
    await client.fetch_balance()


async def test_get_transactions():
    await client.fetch_transactions()


async def test_get_invoices():
    await client.fetch_invoices()


async def test_get_invoice():
    await client.fetch_invoice(1)
