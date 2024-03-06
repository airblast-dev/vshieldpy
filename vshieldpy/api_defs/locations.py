from enum import Enum


class Locations(Enum):
    """Locations that are accepted by the API."""

    Canada = ("Canada",)
    France = ("France",)
    Europe = ("Europe",)
    US = ("US",)
    Singapore = "Singapore"
    UK = ("UK",)
    Netherlands = "Netherlands"

    @staticmethod
    def location_from_short(short_name: str) -> "Locations":
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
