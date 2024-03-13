import pytest

from . import client

pytestmark = pytest.mark.anyio


async def test_server_stats():
    server_stats = await client.fetch_server_stats(1)
    assert server_stats.cpu_avg_last_1hr == 1
    assert server_stats.cpu_avg_last_24hrs == 1

    assert 4.764 > server_stats.ram_avg_last_1hr > 4.763
    assert 4.764 > server_stats.ram_avg_last_24hrs > 4.763

    download, upload = server_stats.network_avg_last_1hr
    assert 0.104 > download > 0.10
    assert 0.067 > upload > 0.066

    download, upload = server_stats.network_avg_last_24hrs
    assert 0.104 > download > 0.10
    assert 0.067 > upload > 0.066
