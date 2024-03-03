import os
import pytest

from vshieldpy.api_defs.auto_renew import AutoRenew
from vshieldpy.api_defs.operating_systems import OperatingSystems
from vshieldpy.api_defs.payment import Payment
from vshieldpy.api_defs.plans import Plans
from vshieldpy.api_defs.tasks import ServerActions
from vshieldpy.exceptions.parameter_exceptions import (
    InvalidHostname,
    ReinstallWithoutOS,
)

os.environ["VS_API_URL"] = "https://localhost:5000"

from vshieldpy.api_defs.graphs import ServerStats
from vshieldpy.products.server import Server, Servers
from vshieldpy.client import Client


pytestmark = pytest.mark.anyio
client = Client("1")


async def test_server_get_list():
    server_list = await client.fetch_servers()
    assert len(server_list) == 2
    assert isinstance(server_list, Servers)


async def test_server_get_info():
    server = await client.fetch_server(1)
    assert isinstance(server, Server)


async def test_server_graphs():
    graph = await client.fetch_server_stats(0)
    assert isinstance(graph, ServerStats)


async def test_server_console():
    console_url = await client.fetch_server_console(0)


async def test_server_create_task():
    await client.create_server_task(
        0, ServerActions.Reinstall, OperatingSystems.Ubuntu20
    )
    with pytest.raises(ReinstallWithoutOS):
        await client.create_server_task(0, ServerActions.Reinstall, None)


async def test_server_manage_autorenew():
    status = await client.set_server_auto_renew(0, AutoRenew.Disable)
    assert status == AutoRenew.Disable


async def test_server_update_hostname():
    new_hostname = await client.set_server_hostname(0, "SteinsGate")
    assert isinstance(new_hostname, str)
    with pytest.raises(InvalidHostname):
        await client.set_server_hostname(0, str(list(range(0, 20))))


async def test_server_upgrade():
    payment = await client.upgrade_server(0, Plans.VDS_PRO_GOLD)
    assert isinstance(payment, Payment)


async def test_server_change_ip():
    payment = await client.change_server_ip(0)
    assert isinstance(payment, Payment)


async def test_server_renew():
    payment = await client.renew_server(0, 100)
    assert isinstance(payment, Payment)


async def test_server_delete():
    task_id = await client.delete_server(0)
    assert isinstance(task_id, int)


async def test_server_order():
    payment = await client.order_server(
        Plans.VDS_PRO_GOLD, "us", "Hello", OperatingSystems.Ubuntu20, 10
    )
    assert isinstance(payment, Payment)
