"""Location related items."""

from __future__ import annotations

from enum import Enum
from typing import Literal

_SHORT_LOCATIONS = Literal["ca", "fr", "eu", "us", "sg", "uk", "nl"]


class Locations(Enum):
    """Locations that are accepted by the API."""

    # NOTE: Since the locations dont abide by any standard, we must make sure these are updated once a new location is added on the API.
    # Sadly this requires manual testing to figure out the accepted labels.

    Canada = "Canada"
    France = "France"
    Europe = "Europe"
    US = "US"
    Singapore = "Singapore"
    UK = "UK"
    Netherlands = "Netherlands"

    @staticmethod
    def location_from_short(short_name: _SHORT_LOCATIONS) -> "Locations":
        """Method to get a location variant by its short name.

        This isnt strictly from ISO3166-2 as the API documentation doesnt specify any standard, nor does it use any based on current knowledge.

        Raises:
            ValueError: In case a location wasnt able to matched with the provided short name.
                        Mainly intended to be called internally.

        Returns:
            Locations: The matching location for the provided short name.
        """
        match short_name.lower():
            case "ca":
                return Locations.Canada
            case "fr":
                return Locations.France
            case "eu":
                return Locations.Europe
            case "us":
                return Locations.US
            case "sg":
                return Locations.Singapore
            case "uk":
                return Locations.UK
            case "nl":
                return Locations.Netherlands
        raise ValueError("Not a know location was returned by the vShield API.")
