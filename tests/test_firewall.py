import os
import pytest

os.environ["VS_API_URL"] = "https://localhost:5000"

from vshieldpy import Client

client = Client("1")

pytestmark = pytest.mark.anyio


async def test_firewall_get_info():
    await client.fetch_firewall(1)
