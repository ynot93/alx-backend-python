#!/usr/bin/env python3
"""
This module deals with unittests and integration tests

"""
import unittest
from unittest.mock import Mock
from utils import access_nested_map
from parameterized import parameterized
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """
    Includes unit tests for the function utils.access_nested_map

    """
    @parameterized.expand([
        ("nested_map1", {"a": 1}, ["a"], 1),
        ("nested_map2", {"a": {"b": 2}}, ["a"], {"b": 2}),
        ("nested_map3", {"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_app(self,
                               name: str,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Any) -> None:
        """
        Test correct return value of method

        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
