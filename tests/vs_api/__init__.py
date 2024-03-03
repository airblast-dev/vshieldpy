"""The webserver for testing the API.

Any responses sent must be same as the examples as the documentation.
Only exceptions to this rule are were all outcomes are same for said example,
and were they need updating based on changes to service in general.

The last one would include things such as locations being added or removed and so on.
"""

from .ws import app
