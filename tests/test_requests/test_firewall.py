import pytest
from test_api import client

from vshieldpy.products.firewall import Firewall

pytestmark = pytest.mark.anyio


async def test_firewall_get_info():
    firewall = await client.fetch_firewall(1)
    assert type(firewall) == Firewall
