"""Module for all API methods and paths."""

from dataclasses import dataclass
from typing import ClassVar, Literal

from .request import _VsUrl

_CVarVsUrl = ClassVar[_VsUrl]
_Methods = Literal["GET", "POST"]


@dataclass(slots=True, frozen=True)
class _SystemRequests:
    GET_PLANS = ("GET", _VsUrl("/system/getPlans"))
    GET_PENDING_ORDERS = ("GET", _VsUrl("/system/getPendingOrders"))
    GET_TASK_INFO = ("GET", _VsUrl("/system/getTaskInfo/"))


@dataclass(slots=True, frozen=True)
class _ServiceRequests:
    GET_LIST = ("GET", _VsUrl("/service/getList"))
    GET_INFO = ("GET", _VsUrl("/service/getInfo/"))
    CREATE_TASK = ("POST", _VsUrl("/service/createTask/"))
    SET_AUTO_RENEW = ("POST", _VsUrl("/service/manageAutoRenew/"))
    RENEW_SERVICE = ("POST", _VsUrl("/service/renew/"))


@dataclass(slots=True, frozen=True)
class _ServerRequests:
    GET_LIST = ("GET", _VsUrl("/server/getList"))
    GET_INFO = ("GET", _VsUrl("/server/getInfo/"))
    GET_GRAPHS = ("GET", _VsUrl("/server/getGraphs/"))
    GET_CONSOLE = ("GET", _VsUrl("/server/console/"))
    CREATE_TASK = ("POST", _VsUrl("/server/createTask/"))
    SET_AUTO_RENEW = ("POST", _VsUrl("/server/manageAutoRenew/"))
    SET_HOSTNAME = ("POST", _VsUrl("/server/updateHostname/"))
    UPGRADE_SERVER = ("POST", _VsUrl("/server/upgrade/"))
    CHANGE_IP = ("POST", _VsUrl("/server/changeIp/"))
    RENEW_SERVER = ("POST", _VsUrl("/server/renew/"))
    DELETE_SERVER = ("POST", _VsUrl("/server/delete/"))
    ORDER_SERVER = ("POST", _VsUrl("/server/order"))


@dataclass(slots=True, frozen=True)
class _BillingRequests:
    GET_BALANCE = ("GET", _VsUrl("/billing/getBalance"))
    GET_TRANSACTIONS = ("GET", _VsUrl("/billing/getTransactions"))
    GET_INVOICES = ("GET", _VsUrl("/billing/getInvoices"))
    GET_INVOICE_INFO = ("GET", _VsUrl("/billing/getInvoiceInfo/"))


@dataclass(slots=True, frozen=True)
class _FirewallRequests:
    GET_INFO = ("GET", _VsUrl("/firewall/getInfo/"))
