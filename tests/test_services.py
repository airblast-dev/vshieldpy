import os

os.environ["VS_API_URL"] = "https://localhost:5000"

from vshieldpy.api_defs.auto_renew import AutoRenew
from vshieldpy.api_defs.operating_systems import OperatingSystems
from vshieldpy.api_defs.tasks import ServiceActions
from vshieldpy.client import Client
import pytest

from vshieldpy.exceptions.parameter_exceptions import ReinstallWithoutOS
from vshieldpy.products.service import Hosting


client = Client("1")

pytestmark = pytest.mark.anyio


async def test_get_service_list():
    services = await client.fetch_services()
    assert len(services.hostings) == 1
    assert len(services.dedicated_servers) == 1
    assert services.hostings[0].status
    assert services.dedicated_servers[0].status


async def test_get_service_info():
    service_info = await client.fetch_service(0)
    assert service_info is not None
    assert service_info.status
    assert service_info
    assert isinstance(service_info, Hosting)


async def test_create_task_service():
    task = await client.create_service_task(
        1, ServiceActions.Reinstall, OperatingSystems.Ubuntu20
    )
    assert task

    with pytest.raises(ReinstallWithoutOS):
        await client.create_service_task(1, ServiceActions.Reinstall, None)


async def test_service_manage_auto_renew():
    new_renew_state = await client.set_service_auto_renew(1, AutoRenew.Enable)
    assert 1 == new_renew_state.value


async def test_service_renew():
    payment = await client.renew_service(1, 3)
    assert payment.new_balance == "0.00"
    assert payment.invoice_id is None
    assert payment.price == "14.99"
