import os
from threading import Thread

import pytest
from vs_api import app

os.environ["VS_API_URL"] = "http://localhost:5000"

#  TODO: Remove noqa once exception case os.environ is added in stable for ruff.
#  https://docs.astral.sh/ruff/rules/module-import-not-at-top-of-file/
import vshieldpy  # noqa

from vshieldpy.api_defs.plans import Plans
from vshieldpy.products.service import Hosting
from vshieldpy.api_defs.status_codes import Status
from vshieldpy.api_defs.tasks import Actions, ServiceActions, TaskStatus
from vshieldpy.api_defs.stocks import StockStatus
from vshieldpy.api_defs.operating_systems import OperatingSystems
from vshieldpy.exceptions.parameter_exceptions import ReinstallWithoutOS

thread = Thread(
    target=app.run,
    daemon=True,
    kwargs={
        "host": "localhost",
        "port": 5000,
    },
)
thread.start()
pytestmark = pytest.mark.anyio


def test_client():
    from vshieldpy.exceptions import auth_exceptions

    global client
    # Test valid base16 auth.
    client = vshieldpy.Client("12")

    # Test invalid base16 auth.
    with pytest.raises(auth_exceptions.InvalidAuthKey):
        vshieldpy.Client("This isnt base16 lmao")


# TODO: Implement testing after better location system.
async def test_system_get_plans(): ...


# TODO: Implement testing after better location system.
async def test_get_pending_orders(): ...


async def test_get_task_info():
    task_info = await client.fetch_task_info(1)
    assert task_info.status == TaskStatus.Completed
    assert task_info.action == Actions.Start
