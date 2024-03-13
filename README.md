# vshieldpy
A library designed to ease the use of the vShield API when using python.
Almost all functionality of the API is implemented, and with proper exceptions.

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Read the Docs](https://readthedocs.org/projects/vshieldpy/badge/?version=latest)](https://vshieldpy.readthedocs.io/en/latest)
[![Testing and Linting](https://github.com/airblast-dev/vshieldpy/actions/workflows/python-package.yml/badge.svg)](https://github.com/airblast-dev/vshieldpy/actions/workflows/python-package.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **_NOTE:_** This is an unofficial library for the vShield API. There-for vShield is not responsible for any issues regarding this library.

[![vShield Blue Banner](https://github.com/airblast-dev/vshieldpy/assets/111659262/c2f54e9e-a9cd-4ee4-936e-6af78f4248e1)](https://vshield.com)

## Supported Products:

All products do have support, however virtual servers (VPS, VDS and VDS-PRO)
have priority in testing and ease of use as that is what I can test for. 

## Documentation:

### Online Version:

You can read the online version of the documentation [here](https://vshieldpy.readthedocs.io/en/latest/). You can also download the offline version from the documentation page if preferred.

### Building it yourself:

After cloning the repository, you must install the library with the "docs" tag.
```bash
python -m pip install ".[docs]"
```
Once it is done, all of the dependencies required to build the documentation will be installed.

You can now build the documentation with a single command.
```bash
python -m sphinx docs/ docs/_build
```

The built documentation will be stored in the `docs/_build` directory of the project. 
Now you can simply open the `index.html` file in your browser of choice, and get started.


## Examples:

### REPL:
Example for creating a client and sending a request to check the accounts current balance.
		
```python-repl
>>> # For use via the repl, "python -m asyncio" is more practical since its easier to use with async functions.
>>> from vshieldpy import Client
>>> client = Client("YOUR_TOKEN")
>>> await client.fetch_balance()
'0.00'
```

> **_NOTE:_** For an implementation example in an application such as a discord bot, feel free to check out the [examples](examples/README.md).

## Contribution:
The library does cover all API paths, however, there are a few small things missing.
- Setting a wallpaper for a server. (This is only doable if you have reseller access)
- Tasks are not stored in the instance of a server, said tasks are only returned by `/server/getInfo/<server_id>`.
- The ease of use of the library might be lacking for various use cases such as hosting a reseller website. I am open to ways this can be improved.
- Implementing testing for exceptions. Most important ones are already implemented, however a few (mainly parameter exceptions) are not tested.

For non-breaking and/or small changes feel free to create a PR. If not create an issue so a solution can be discussed.

You can install all the dependencies needed for development using the "dev" tag as shown below.
```bash
pip install ".[dev]"
```
This will install the dev dependencies needed for testing, linting, and formatting.

For formatting and linting [ruff](https://github.com/astral-sh/ruff) is used.

You can run `python -m ruff check`, and `python -m ruff format` in the project to check if there is any issues.

For testing [pytest](https://github.com/pytest-dev/pytest) is used.

You can simply run `python -m pytest` in the project directory to start the tests.
