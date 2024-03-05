"""Module for constructing vShield API URL's and related functions."""

from os import getenv

from httpx import URL

# Env variable should only be used if vShields API path is changed, or for testing purposes.
VS_API_URL = getenv("VS_API_URL") or "https://api.vshield.pro"


def _url_factory(url: str) -> URL:
    """:class:`URL` factory for constructing vShield API paths."""
    return URL(VS_API_URL + url)
