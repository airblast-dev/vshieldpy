import pytest

from test_api import client

pytestmark = pytest.mark.anyio


async def test_firewall_get_info():
    await client.fetch_firewall(1)
