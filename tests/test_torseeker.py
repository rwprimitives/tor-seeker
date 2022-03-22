#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit testing for TorSeeker

Note:
It is assumed that TorSeeker is already installed.
"""

import unittest

from torseeker import torseeker


class TorSeekerTests(unittest.TestCase):
    def setUp(self):
        self.TS = torseeker.TorSeeker()

    def test_valid_country(self):
        self.assertTrue(self.TS.query_relays_by_country("cr"))

    def test_invalid_country(self):
        self.assertEqual(self.TS.query_relays_by_country("xx"), 0)

    def test_empty_country(self):
        self.assertEqual(self.TS.query_relays_by_country(), 0)

    def test_none_country(self):
        self.assertEqual(self.TS.query_relays_by_country(None), 0)

    def test_valid_ipaddress_list(self):
        # These test IP addresses are of Tor Authority nodes which should
        # rarely ever change.
        moria1_authority = "128.31.0.34"
        faravahar_authority = "154.35.175.225"

        ip_list = []
        ip_list.append(moria1_authority)
        ip_list.append(faravahar_authority)
        self.assertTrue(self.TS.query_relays_by_ip(ip_list))

    def test_empty_ipaddress_list(self):
        ip_list = []
        self.assertEqual(self.TS.query_relays_by_ip(ip_list), 0)

    def test_none_ipaddress_list(self):
        self.assertEqual(self.TS.query_relays_by_ip(None), 0)

    def test_non_tor_ipaddress_list(self):
        ip_list = []
        ip_list.append("1.1.1.1")
        ip_list.append("8.8.8.8")
        self.assertEqual(self.TS.query_relays_by_ip(), 0)


if __name__ == '__main__':
    unittest.main()
