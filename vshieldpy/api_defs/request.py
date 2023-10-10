"""Module for constructing vShield API URL's and related functions."""


from __future__ import annotations

from httpx import URL

BASE_API_URL = "https://api.vshield.pro"


class _VsUrl(URL):
    """Url object for constructing vShield API paths."""

    def __init__(self, url: str):
        super().__init__(BASE_API_URL + url)
