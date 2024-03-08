from datetime import datetime

import pytest

from vshieldpy.api_defs.auto_renew import AutoRenew
from vshieldpy.api_defs.operating_systems import OperatingSystems
from vshieldpy.api_defs.plans import Plans
from vshieldpy.api_defs.status_codes import Status
from vshieldpy.client import Client
from vshieldpy.products import Server, Servers

pytestmark = pytest.mark.anyio

client = Client()

SERVERS: tuple[Server, ...] = (
    Server(
        1,
        "192.168.1.1",
        "testhostname",
        OperatingSystems.Ubuntu20,
        Plans.VDS_PRO_ENTERPRISE,
        AutoRenew.Enable,
        Status.Running,
        "ca11",
        datetime.now(),
        datetime.now(),
        "supersecret",
    ),
    Server(
        2,
        "192.168.1.2",
        "dumbname",
        OperatingSystems.Ubuntu20,
        Plans.VDS_PRO_ENTERPRISE,
        AutoRenew.Enable,
        Status.Running,
        "ca12",
        datetime.now(),
        datetime.now(),
        "supersecret",
    ),
)


def test_servers():
    hostname = "dumbname"
    assert all(
        [
            server.hostname == hostname
            for server in Servers(SERVERS).get_server_from_hostname(hostname)
        ]
    )


async def test_server():
    server = SERVERS[0]
    server._client = client
    await server.refresh()
    assert isinstance(server.password, str)
