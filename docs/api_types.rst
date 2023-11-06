API Types
==============

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

API types are objects returned by calls that return non product responses from :doc:`Client <client>`. So this would include things like tasks, stock statuses and auto-renew settings but exclude a server, dedicated server and hosting.
There really isnt a reason to import these beyond type annotating.

.. autoclass:: vshieldpy.api_defs.Invoice()
   :members:
   :exclude-members: dataclass

.. autoclass:: vshieldpy.api_defs.StockStatus()
   :members:
   :exclude-members: dataclass

.. autoclass:: vshieldpy.api_defs.Task()
   :members:
   :exclude-members: dataclass

.. autoclass:: vshieldpy.api_defs.Payment()
   :members:
   :exclude-members: dataclass

.. autoclass:: vshieldpy.api_defs.ServerStats()
   :members:
   :exclude-members: dataclass

.. autoenum:: vshieldpy.api_defs.TaskStatus
   :members:

.. autoenum:: vshieldpy.api_defs.Status
   :members:

