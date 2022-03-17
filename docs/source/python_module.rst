Importing as Module
===================

This section will walk through the different ways **TorSeeker** can be imported as a Python module.


Import via Interpreter
-----------------------

Here is an example of how you would use it with the Python interactive interpreter:

.. code-block:: console

    >>> from torseeker import torseeker
    >>> ts = torseeker.TorSeeker()
    >>> ts = torseeker.TorSeeker()
    >>> ts.query_relays_by_country("br")
    1
    >>> torseeker.print_relay_info(ts.get_exit_relays())
    187.20.55.213   | Port: 9090, Nickname: arbitrium, Country: Brazil, First seen: 2017-08-08 19:00:00, Last seen: 2022-02-21 20:00:00, Last restarted: 2022-01-31 22:07:13
    189.84.21.44    | Port: 443, Nickname: tauro, Country: Brazil, First seen: 2016-03-23 17:00:00, Last seen: 2022-02-21 20:00:00, Last restarted: 2022-02-03 14:16:15
