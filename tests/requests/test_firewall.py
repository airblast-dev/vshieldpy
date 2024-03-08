import pytest

from vshieldpy.products.firewall import Firewall

from . import client

pytestmark = pytest.mark.anyio


async def test_firewall_get_info():
    firewall = await client.fetch_firewall(1)
    assert type(firewall) == Firewall
