## vshieldpy
A library designed to ease the use of the vShield API when using python.
Almost all functionality of the API is implemented and with (mostly) proper exceptions.

> **_NOTE:_** This is an unofficial library for the vShield API. There-for vShield is not responsible for any issues regarding this library.

> **_WARNING_** The library is in its early stages this means breaking changes are made very often. Beware!

<a href="https://vshield.pro"><img src="https://cdn.discordapp.com/attachments/1048581891411951636/1170771111361917008/bannerblue.png?ex=655a4090&is=6547cb90&hm=a0579448a362ca4b2c9dc8014ed765d0c7579ecd19043c6a24dd65e6981edbcf&"></a>

In case of any issues using the library, be it better exception handling or ease of use ... feel free to create an issue on Github.

### Supported Products:

All products do have support, however virtual servers (VPS, VDS and VDS-PRO)
have priority in testing and ease of use as that is what I can test for. 

### Documentation:

The library has complete documentation made with sphinx. You can build the documentation yourself using sphinx-build. An online version will be posted soon.

To install sphinx and the sphinx extension dependencies install the project with the docs tag as shown here `pip install ".[docs]"` .

### Examples:

#### REPL:
Example for creating a client and sending a request to check the accounts current balance.
		
```python-repl
>>> # For use via the repl, "python -m asyncio" is more practical since its easier to use with async functions.
>>> from vshieldpy import Client
>>> client = Client("YOUR_TOKEN")
>>> await client.fetch_balance()
'0.00'
```

> **_NOTE:_** For an implementation example in an application such as a discord bot, feel free to check out the [examples](examples/EXAMPLES.md).
