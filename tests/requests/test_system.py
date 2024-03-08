import pytest

from vshieldpy.api_defs.stocks import StockStatus
from vshieldpy.api_defs.tasks import Task
from vshieldpy.products.server import PendingServer

from . import client

pytestmark = pytest.mark.anyio


async def test_get_plans():
    plans = await client.fetch_plans()
    assert type(plans) == StockStatus


async def test_get_pending_oreders():
    pending_orders = await client.fetch_pending_orders()
    assert all([type(pending) == PendingServer for pending in pending_orders])


async def test_get_task_info():
    task_info = await client.fetch_task_info(1)
    assert type(task_info) == Task
