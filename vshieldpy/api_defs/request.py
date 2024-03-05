"""Module for constructing vShield API URL's and related functions."""

from __future__ import annotations

from os import getenv

from httpx import URL

# Env variable should only be used if vShields API path is changed, or for testing purposes.
VS_API_URL = getenv("VS_API_URL") or "https://api.vshield.pro"


class _VsUrl(URL):
    """Url object for constructing vShield API paths."""

    def __init__(self, url: str):
        super().__init__(VS_API_URL + url)
