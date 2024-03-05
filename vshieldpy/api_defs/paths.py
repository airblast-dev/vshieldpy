"""Module for all API methods and paths."""

from dataclasses import dataclass
from typing import Literal

from .request import _url_factory

_Methods = Literal["GET", "POST"]


@dataclass(slots=True, frozen=True)
class _SystemRequests:
    GET_PLANS = ("GET", _url_factory("/system/getPlans"))
    GET_PENDING_ORDERS = ("GET", _url_factory("/system/getPendingOrders"))
    GET_TASK_INFO = ("GET", _url_factory("/system/getTaskInfo/"))


@dataclass(slots=True, frozen=True)
class _ServiceRequests:
    GET_LIST = ("GET", _url_factory("/service/getList"))
    GET_INFO = ("GET", _url_factory("/service/getInfo/"))
    CREATE_TASK = ("POST", _url_factory("/service/createTask/"))
    SET_AUTO_RENEW = ("POST", _url_factory("/service/manageAutoRenew/"))
    RENEW_SERVICE = ("POST", _url_factory("/service/renew/"))


@dataclass(slots=True, frozen=True)
class _ServerRequests:
    GET_LIST = ("GET", _url_factory("/server/getList"))
    GET_INFO = ("GET", _url_factory("/server/getInfo/"))
    GET_GRAPHS = ("GET", _url_factory("/server/getGraphs/"))
    GET_CONSOLE = ("GET", _url_factory("/server/console/"))
    CREATE_TASK = ("POST", _url_factory("/server/createTask/"))
    SET_AUTO_RENEW = ("POST", _url_factory("/server/manageAutoRenew/"))
    SET_HOSTNAME = ("POST", _url_factory("/server/updateHostname/"))
    UPGRADE_SERVER = ("POST", _url_factory("/server/upgrade/"))
    CHANGE_IP = ("POST", _url_factory("/server/changeIp/"))
    RENEW_SERVER = ("POST", _url_factory("/server/renew/"))
    DELETE_SERVER = ("POST", _url_factory("/server/delete/"))
    ORDER_SERVER = ("POST", _url_factory("/server/order"))


@dataclass(slots=True, frozen=True)
class _BillingRequests:
    GET_BALANCE = ("GET", _url_factory("/billing/getBalance"))
    GET_TRANSACTIONS = ("GET", _url_factory("/billing/getTransactions"))
    GET_INVOICES = ("GET", _url_factory("/billing/getInvoices"))
    GET_INVOICE_INFO = ("GET", _url_factory("/billing/getInvoiceInfo/"))


@dataclass(slots=True, frozen=True)
class _FirewallRequests:
    GET_INFO = ("GET", _url_factory("/firewall/getInfo/"))
