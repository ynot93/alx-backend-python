#!/usr/bin/env python3
"""
This module deals with unittests and integration tests

"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict


class TestAccessNestedMap(unittest.TestCase):
    """
    Includes unit tests for the function utils.access_nested_map

    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_app(self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        """
        Test correct return value of method

        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence) -> None:
        """
        Test raises KeyError with the expected message

        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """
    Contains tests for the get_json function in utils.py

    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get) -> None:
        """
        Test that function returns expected result

        """
        mock_object = Mock()
        mock_object.json.return_value = test_payload
        mock_get.return_value = mock_object

        result = get_json(test_url)

        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Contatins tests for the utils.memoize function

    """
    def test_memoize(self) -> None:
        """
        Tests that using memoize caches the result of an operation

        """
        class TestClass:
            """Tests the memoize function"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        
        with patch.object(TestClass, 'a_method', return_value=42) as mock_object:
            my_test_class = TestClass()
            
            result1 = my_test_class.a_property
            result2 = my_test_class.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_object.assert_called_once()


if __name__ == "__main__":
    unittest.main()
