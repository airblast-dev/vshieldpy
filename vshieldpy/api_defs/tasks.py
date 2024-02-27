"""Module for tasks and performable actions."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Actions(Enum):
    """All possible actions that can be performed on a service or server."""

    Start = "start"
    Stop = "stop"
    Reinstall = "reinstall"
    Restart = "restart"
    FixNetwork = "fixnetwork"
    ChangePass = "changepass"
    RenewLicense = "renewlicense"


class ServiceActions(Enum):
    """Actions that can be performed on a Dedicated Server."""

    Start = "start"
    Stop = "stop"
    Reinstall = "reinstall"
    Restart = "restart"


class ServerActions(Enum):
    """Actions that can be performed on a server."""

    Start = "start"
    Stop = "stop"
    Reinstall = "reinstall"
    Restart = "restart"
    FixNetwork = "fixnetwork"
    ChangePass = "changepass"
    RenewLicense = "renewlicense"


class TaskStatus(Enum):
    """Possible task statuses."""

    Failed = 0
    Completed = 1
    InProgress = 2


@dataclass(init=True, slots=True)
class Task:
    """A task and all of its information.

    Attributes:
        action: Server or service action that was performed or being performed.
        completion_date: Time of the task completion.
        start_date: Time of when the task was started.
        status: Current status of the task.
    """

    action: Actions
    completion_date: datetime
    start_date: datetime
    status: TaskStatus
