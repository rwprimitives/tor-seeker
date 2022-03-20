Command Line
============

This section walks you through the different ways **TorSeeker** can be used as a command line tool.


Basic Usage
-----------

**TorSeeker** provides two simple methods for querying information about Tor relays. A query can be performed by specifying a two letter country code or by using one or multiple Tor IP addresses. The end result will be the same.


Synopsis
--------

To view the different options supported, execute `torseeker` with `-h` or `- -help` option:

.. code-block:: console

    usage: torseeker [-h] [-d] [-v] (-c  | --ip  [...])

    A tool used to query information about Tor relays by using a two 
    letter country code or via Tor IP addresses.

    optional arguments:
      -h, --help       show this help message and exit
      -d, --details    show additional information
      -v               show program's version number and exit
      -c , --country   two letter country code of interest
      --ip  [ ...]     one or more tor IP addresses spaced separated


Query Tor relays by Country
---------------------------

The following example shows how to use `-c` option with the two letter country code for Costa Rica: 

.. code-block:: console

    $ torseeker -c cr

      ______           _____           __            
     /_  __/___  _____/ ___/___  ___  / /_____  _____
      / / / __ \/ ___/\__ \/ _ \/ _ \/ //_/ _ \/ ___/
     / / / /_/ / /   ___/ /  __/  __/ ,< /  __/ /    
    /_/  \____/_/   /____/\___/\___/_/|_|\___/_/     
        
    1.0.0 by eldiablo

    Country: Costa Rica
    Total relays: 11
    Guard relays: 3
    Middle relays: 4
    Exit relays: 5


Using the same command and specify the `-d` option to get additional information about the relays:

.. code-block:: console

    $ torseeker -c cr -d

      ______           _____           __            
     /_  __/___  _____/ ___/___  ___  / /_____  _____
      / / / __ \/ ___/\__ \/ _ \/ _ \/ //_/ _ \/ ___/
     / / / /_/ / /   ___/ /  __/  __/ ,< /  __/ /    
    /_/  \____/_/   /____/\___/\___/_/|_|\___/_/     
        
    1.0.0 by eldiablo

    Country: Costa Rica
    Total relays: 11
    Guard relays: 3
    Middle relays: 4
    Exit relays: 5


    GUARD RELAYS
    ------------
    138.59.18.106   | Port: 443, Nickname: Albis, Country: Costa Rica, First seen: 2019-02-20 21:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2021-11-13 06:06:04
    138.59.18.105   | Port: 88, Nickname: TheMind, Country: Costa Rica, First seen: 2019-02-20 14:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2021-10-29 16:06:04
    138.59.18.110   | Port: 443, Nickname: demonteal, Country: Costa Rica, First seen: 2019-05-14 18:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2022-01-11 18:41:11


    MIDDLE RELAYS
    -------------
    200.122.181.101 | Port: 443, Nickname: Karai, Country: Costa Rica, First seen: 2018-01-11 14:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2021-10-21 11:21:08
    190.10.8.50     | Port: 443, Nickname: cragg, Country: Costa Rica, First seen: 2019-10-31 15:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2022-01-04 21:26:19
    190.10.8.68     | Port: 443, Nickname: cressington, Country: Costa Rica, First seen: 2016-04-08 16:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2022-01-08 22:56:28
    200.122.181.78  | Port: 443, Nickname: Splinter, Country: Costa Rica, First seen: 2018-01-17 20:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2021-06-30 21:23:25


    EXIT RELAYS
    -----------
    138.59.17.40    | Port: 443, Nickname: barwin, Country: Costa Rica, First seen: 2020-02-06 18:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2021-11-24 10:22:18, IPv6: 2803:6900:533:1:216:3eff:fe70:a38, IPv6 Port: 443
    179.48.251.188  | Port: 443, Nickname: toritico01, Country: Costa Rica, First seen: 2019-02-13 15:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2021-06-08 19:40:19
    200.122.181.2   | Port: 443, Nickname: Michelangelo, Country: Costa Rica, First seen: 2020-10-02 16:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2021-06-18 03:22:29
    138.59.18.110   | Port: 443, Nickname: demonteal, Country: Costa Rica, First seen: 2019-05-14 18:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2022-01-11 18:41:11
    190.10.8.166    | Port: 443, Nickname: Donatello, Country: Costa Rica, First seen: 2021-03-12 20:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2022-01-04 22:48:54


Query Tor relays via IP address
-------------------------------

The following example shows how to use `- -ip` option with two Tor relay IP addresses: 

.. code-block:: console

    $ torseeker --ip 138.59.18.106 190.10.8.166
      ______           _____           __            
     /_  __/___  _____/ ___/___  ___  / /_____  _____
      / / / __ \/ ___/\__ \/ _ \/ _ \/ //_/ _ \/ ___/
     / / / /_/ / /   ___/ /  __/  __/ ,< /  __/ /    
    /_/  \____/_/   /____/\___/\___/_/|_|\___/_/     

    1.0.0 by eldiablo

    Total relays: 2
    Guard relays: 1
    Middle relays: 0
    Exit relays: 1

Using the same command and specify the `-d` option to get additional information about the relays:

.. code-block:: console

    $ torseeker --ip 138.59.18.106 190.10.8.166 -d

      ______           _____           __            
     /_  __/___  _____/ ___/___  ___  / /_____  _____
      / / / __ \/ ___/\__ \/ _ \/ _ \/ //_/ _ \/ ___/
     / / / /_/ / /   ___/ /  __/  __/ ,< /  __/ /    
    /_/  \____/_/   /____/\___/\___/_/|_|\___/_/     
        
    1.0.0 by eldiablo

    Total relays: 2
    Guard relays: 1
    Middle relays: 0
    Exit relays: 1


    GUARD RELAYS
    ------------
    138.59.18.106   | Port: 443, Nickname: Albis, Country: Costa Rica, First seen: 2019-02-20 21:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2021-11-13 06:06:04


    MIDDLE RELAYS
    -------------
    None


    EXIT RELAYS
    -----------
    190.10.8.166    | Port: 443, Nickname: Donatello, Country: Costa Rica, First seen: 2021-03-12 20:00:00, Last seen: 2022-02-13 03:00:00, Last restarted: 2022-01-04 22:48:54
