TorSeeker For Developers
========================

This section will walk through the different ways **TorSeeker** can be imported as a Python module.


Import via Interpreter
-----------------------

Here is an example of how you would import **TorSeeker** via the Python interactive interpreter:

.. code-block:: console

    >>> from torseeker import torseeker
    >>> ts = torseeker.TorSeeker()
    >>> ts.query_relays_by_country("cr")
    1
    >>> torseeker.print_relay_info(ts.get_exit_relays())
    138.59.17.40    | Port: 443, Nickname: barwin, Country: Costa Rica, First seen: 2020-02-06 18:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2021-11-24 10:22:18, IPv6: 2803:6900:533:1:216:3eff:fe70:a38, IPv6 Port: 443
    179.48.251.188  | Port: 443, Nickname: toritico01, Country: Costa Rica, First seen: 2019-02-13 15:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-02-21 10:10:31
    200.122.181.2   | Port: 443, Nickname: Michelangelo, Country: Costa Rica, First seen: 2020-10-02 16:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-03-16 19:11:08
    138.59.18.110   | Port: 443, Nickname: demonteal, Country: Costa Rica, First seen: 2019-05-14 18:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-03-23 12:51:11
    190.10.8.166    | Port: 443, Nickname: Donatello, Country: Costa Rica, First seen: 2021-03-12 20:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-01-04 22:48:54


Importing via Python Script
---------------------------

The following example shows how to import **TorSeeker** into your own Python script and perform queries:

.. code-block:: python

    #!/usr/bin/env python3

    from torseeker import torseeker

    tor_seeker = torseeker.TorSeeker()

    # Enable logging
    tor_seeker.set_logging(True)

    # Query Tor relays located in Costa Rica
    tor_seeker.query_relays_by_country("cr")

    # Iterate through all of the relays and print out each Tor node
    for relay in tor_seeker.get_all_relays():
        print(relay)


Below is the output of the script above:

.. code-block:: console

    138.59.18.106   | Port: 443, Nickname: Albis, Country: Costa Rica, First seen: 2019-02-20 21:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-02-24 02:11:04
    138.59.18.105   | Port: 88, Nickname: TheMind, Country: Costa Rica, First seen: 2019-02-20 14:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-02-17 06:16:04
    138.59.17.40    | Port: 443, Nickname: barwin, Country: Costa Rica, First seen: 2020-02-06 18:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2021-11-24 10:22:18, IPv6: 2803:6900:533:1:216:3eff:fe70:a38, IPv6 Port: 443
    179.48.251.188  | Port: 443, Nickname: toritico01, Country: Costa Rica, First seen: 2019-02-13 15:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-02-21 10:10:31
    200.122.181.101 | Port: 443, Nickname: Karai, Country: Costa Rica, First seen: 2018-01-11 14:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-03-16 19:21:09
    201.192.156.175 | Port: 8118, Nickname: khazad8337, Country: Costa Rica, First seen: 2022-03-19 16:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-03-19 15:20:08
    200.122.181.2   | Port: 443, Nickname: Michelangelo, Country: Costa Rica, First seen: 2020-10-02 16:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-03-16 19:11:08
    138.59.18.110   | Port: 443, Nickname: demonteal, Country: Costa Rica, First seen: 2019-05-14 18:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-03-23 12:51:11
    190.10.8.50     | Port: 443, Nickname: cragg, Country: Costa Rica, First seen: 2019-10-31 15:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-02-19 23:07:03
    190.10.8.68     | Port: 443, Nickname: cressington, Country: Costa Rica, First seen: 2016-04-08 16:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-01-08 22:56:28
    200.122.181.78  | Port: 443, Nickname: Splinter, Country: Costa Rica, First seen: 2018-01-17 20:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2021-06-30 21:23:25
    190.10.8.166    | Port: 443, Nickname: Donatello, Country: Costa Rica, First seen: 2021-03-12 20:00:00, Last seen: 2022-03-24 02:00:00, Last restarted: 2022-01-04 22:48:54
