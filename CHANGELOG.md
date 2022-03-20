Changelog
=========

All notable changes to this project will be documented in this file.

****

[1.0.1] - TBD
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
