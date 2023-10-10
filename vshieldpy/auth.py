"""Moduel for Authentication and its related functions."""

from httpx import Auth


class _VShieldAuth(Auth):
    """Authentication handler for requests to the vShield API."""

    __slots__ = "token"

    def __init__(self, token: str):
        self.token = token

    def auth_flow(self, request):
        request.headers["X-API-KEY"] = self.token
        yield request
