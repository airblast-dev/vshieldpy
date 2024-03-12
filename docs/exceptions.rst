Exceptions
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



##############
Base Exception
##############

All of the exceptions defined in the library are subclassed from this class.

.. warning:: 
   Sadly the error's returned by the API are not documented in any way, so it is recommended to handle this exception where exceptions are being handled in any form.
   In such case that the exception is stated in the API response, but this exception is raised, please create an issue so a proper exceptions can be implemented.

.. autoclass:: vshieldpy.exceptions.base_exception.VShieldpyException
   :members:

########################
Authentication Exception
########################

Authentication related exceptions. Exceptions in this section are expected to be raised in a few cases.

 - The token is structurely invalid (In other words invalidated before a request is even sent.)
 - The token was rejected by the API.
 - A new token was requested via the panel (Which means the old token is invalid.)

.. note:: 
   While it may be obvious, this means the exception could theoretically be raised from any request that is sent to the API.

.. automodule:: vshieldpy.exceptions.auth_exceptions
   :members:


######################
Idenftifier Exceptions
######################

The exceptions in this section can only be raised from functions that take in an identifier of some sort.

.. automodule:: vshieldpy.exceptions.id_exceptions
   :members:

####################
Parameter Exceptions
####################

Exceptions here are most likely to be raised whilst sending a request to order a server.

.. automodule:: vshieldpy.exceptions.parameter_exceptions
   :members:







