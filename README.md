TorSeeker
==========

**TorSeeker** is a command line tool and a Python module that can be used to query information about Tor relays.

From the command line, queries can be performed relatively easy by using a two letter country code or via one or multiple Tor IP addresses.

As a Python module, **TorSeeker** offers a reasonable and easy approach for querying information about Tor relays from within your own Python script or module.

Internet connection is required in order to perform Tor network queries.


Build
=====

This section covers several build aspects of the **TorSeeker** project. 


Required Debian Packages
------------------------

The following packages are required:

| Dependency         | Version           |
|--------------------|-------------------|
| make               | 4.2.1             |
| python3-all        | 3.8.2-0ubuntu2    |
| python3-venv       | 3.8.2-0ubuntu2    |
| python3-setuptools | 45.2.0-1          |
| dh-python          | 4.20191017ubuntu7 |

    sudo apt install make dh-python python3-all python3-venv python3-setuptools


Required PyPi Packages
----------------------

The following PyPi packages are required:

| Dependency | Version | Purpose                                   |
|------------|---------|-------------------------------------------|
| build      | 0.7.0   | Used to build Python distribution package |
| stdeb      | 0.10.0  | Used to build Debian source package       |

    pip install build stdeb


Optional PyPi Packages
----------------------

The following PyPi packages are optional to install:

| Dependency       | Version | Purpose
|------------------|---------|-----------------------------------|
| flake8           | 4.0.1   | Used for checking code style      |
| sphinx_rtd_theme | 4.4.0   | Used for generating documentation |

    pip install flake8 sphinx_rtd_theme


Build Targets
-------------

Once all of the required dependencies have been installed, **TorSeeker** provides several build targets that make it easier to build and deploy.

To view the build targets supported, run the command `make help` as such:

    $ make help

    The following build targets are available:
    
    build-pip:     Generates a PIP distributions packages (ie: *.whl and *.tar.gz)
    build-deb:     Generates a Debian Linux distribution package (ie: *.deb)
    install-pip:   Builds and installs PIP distribution package
    install-deb:   Builds and installs Debian distribution package
    uninstall-pip: Uninstalls PIP distribution package
    uninstall-deb: Uninstalls Debian distribution package
    clean:         Removes any automatically generated files


Installation
============

This section provides several methods for installing **TorSeeker**.


From the Source
---------------

**TorSeeker** can be build and deployed directly from the source. It can be obtained as follows:

    $ git clone https://github.com/rwprimitives/tor-seeker.git


Installing from PyPi
--------------------

It is highly recommended that **TorSeeker** be installed using `pip` to ensure that the latest version is being used.

To install simply run:

    $ pip install torseeker


Command Line
============

This section walks you through the different ways **TorSeeker** can be used as a command line tool.


Basic Usage
-----------

**TorSeeker** provides two simple methods for querying information about Tor relays. A query can be performed by specifying a two letter country code or by using one or multiple Tor IP addresses. The end result will be the same.


Synopsis
--------

To view the different options supported, execute `torseeker` with `-h` or `--help` option:

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

The following example shows how to use `--ip` option with the two Tor relay IP addresses: 

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


Importing as Module
===================

This section will walk through the different ways **TorSeeker** can be imported as a Python module.


Import via Interpreter
-----------------------

Here is an example of how you would use it with the Python interactive interpreter:

    >>> from torseeker import torseeker
    >>> ts = torseeker.TorSeeker()
    >>> ts = torseeker.TorSeeker()
    >>> ts.query_relays_by_country("br")
    1
    >>> torseeker.print_relay_info(ts.get_exit_relays())
    187.20.55.213   | Port: 9090, Nickname: arbitrium, Country: Brazil, First seen: 2017-08-08 19:00:00, Last seen: 2022-02-21 20:00:00, Last restarted: 2022-01-31 22:07:13
    189.84.21.44    | Port: 443, Nickname: tauro, Country: Brazil, First seen: 2016-03-23 17:00:00, Last seen: 2022-02-21 20:00:00, Last restarted: 2022-02-03 14:16:15


Importing via Python Script
---------------------------

The following example shows how to import **TorSeeker** into your own Python script and perform queries:

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

    138.59.18.106   | Port: 443, Nickname: Albis, Country: Costa Rica, First seen: 2019-02-20 21:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2022-02-24 02:11:04
    138.59.18.105   | Port: 88, Nickname: TheMind, Country: Costa Rica, First seen: 2019-02-20 14:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2022-02-17 06:16:04
    138.59.17.40    | Port: 443, Nickname: barwin, Country: Costa Rica, First seen: 2020-02-06 18:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2021-11-24 10:22:18, IPv6: 2803:6900:533:1:216:3eff:fe70:a38, IPv6 Port: 443
    179.48.251.188  | Port: 443, Nickname: toritico01, Country: Costa Rica, First seen: 2019-02-13 15:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2022-02-21 10:10:31
    200.122.181.101 | Port: 443, Nickname: Karai, Country: Costa Rica, First seen: 2018-01-11 14:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2022-03-16 19:21:09
    201.192.156.175 | Port: 8118, Nickname: khazad8337, Country: Costa Rica, First seen: 2022-03-05 14:00:00, Last seen: 2022-03-19 15:00:00, Last restarted: 2022-03-08 17:46:50
    201.192.156.175 | Port: 8118, Nickname: khazad8337, Country: Costa Rica, First seen: 2022-03-19 16:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2022-03-19 15:20:08
    200.122.181.2   | Port: 443, Nickname: Michelangelo, Country: Costa Rica, First seen: 2020-10-02 16:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2022-03-16 19:11:08
    138.59.18.110   | Port: 443, Nickname: demonteal, Country: Costa Rica, First seen: 2019-05-14 18:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2022-03-04 12:06:13
    190.10.8.50     | Port: 443, Nickname: cragg, Country: Costa Rica, First seen: 2019-10-31 15:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2022-02-19 23:07:03
    190.10.8.68     | Port: 443, Nickname: cressington, Country: Costa Rica, First seen: 2016-04-08 16:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2022-01-08 22:56:28
    200.122.181.78  | Port: 443, Nickname: Splinter, Country: Costa Rica, First seen: 2018-01-17 20:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2021-06-30 21:23:25
    190.10.8.166    | Port: 443, Nickname: Donatello, Country: Costa Rica, First seen: 2021-03-12 20:00:00, Last seen: 2022-03-20 18:00:00, Last restarted: 2022-01-04 22:48:54


Contributions
=============

Contributions to the project can be made by doing one of the following:

1. Check for open issues before submitting a feature or bug.
2. Create a new issue to start a discussion around a new feature or a bug.


License
=======

The MIT License

Copyright (c) 2022 rwprimitives

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
