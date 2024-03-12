## vshieldpy
A library designed to ease the use of the vShield API when using python.
Almost all functionality of the API is implemented and with (mostly) proper exceptions.

> **_NOTE:_** This is an unofficial library for the vShield API. There-for vShield is not responsible for any issues regarding this library.

<a href="https://vshield.pro"><img src="https://cdn.discordapp.com/attachments/1048581891411951636/1170771111361917008/bannerblue.png?ex=655a4090&is=6547cb90&hm=a0579448a362ca4b2c9dc8014ed765d0c7579ecd19043c6a24dd65e6981edbcf&"></a>

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

> **_NOTE:_** For an implementation example in an application such as a discord bot, feel free to check out the [examples](examples/README.md).

### Contribution:
The library does cover all API paths, however, there are a few small things missing.
- Setting a wallpaper for a server. (This is only doable if you have reseller access)
- Tasks are not stored in the instance of a server, said tasks are only returned by `/server/getInfo/<server_id>`.
- The ease of use of the library might be lacking for various use cases such as hosting a reseller website.

For non-breaking and/or small changes feel free to create a PR. If not create an issue so a solution can be discussed.
