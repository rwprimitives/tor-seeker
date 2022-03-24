Changelog
=========

All notable changes to this project will be documented in this file.

****

[1.0.2] - 03/23/2022
--------------------
- Fixed bug which resulted in providing inaccurate list of Tor relays types
- Revised README.md and separated Build and Development sections into individual files
- Updated sphinx documentation

[1.0.1] - 03/21/2022
--------------------
- Added sphinx documentation
- Updated README.md to match sphinx documentation
- Added feature to enable/disable logging in `TorSeeker` class
- Fixed `_query()` function to catch json `JSONDecodeError` exception and set return status correctly
- Added IPv4 validation to `query_relays_by_ip()`
- Changed `get_all_relays()` to return a list of `TorNode` objects
- Added requirement.in and requirement-dev.in files to install the necessary required packages

[1.0.0] - 2022-02-13
--------------------
- Initial release
