import pytest

from vshieldpy.api_defs.locations import Locations
from vshieldpy.api_defs.plans import Plans

from . import client

pytestmark = pytest.mark.anyio


async def test_stock_status_check_stock():
    stock_status = await client.fetch_plans()
    assert stock_status.check_stock(Plans.VDS_1, Locations.Netherlands)
    assert stock_status.check_stock(Plans.VDS_2, Locations.Netherlands)
    assert not stock_status.check_stock(Plans.VDS_3, Locations.Netherlands)


async def test_stock_status_get_locations():
    stock_status = await client.fetch_plans()
    assert (Locations.Netherlands, Locations.US) == stock_status.get_locations(
        Plans.VDS_3
    )
    assert (
        Locations.Europe,
        Locations.Singapore,
        Locations.US,
    ) == stock_status.get_locations(Plans.VDS_PRO_BRONZE)
