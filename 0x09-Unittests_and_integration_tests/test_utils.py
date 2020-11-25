#!/usr/bin/env python3
"""Unit tests for utils module"""


import unittest
from unittest import mock
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ A class for testing utils.access_nested_map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, value, path, expected):
        """Sucess testing for access_nested_map method"""
        self.assertEqual(access_nested_map(value, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, value, path, error):
        """ Test utils.test_access_nested_map exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(value, path)
            self.assertEqual(error, str(e.exception))


class TestGetJson(unittest.TestCase):
    """Testing cases for utils.get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Tests utils.get_json"""
        res = mock.Mock()
        res.json.return_value = payload

        with mock.patch('requests.get', return_value=res):
            mock_request = get_json(url)
            res.json.assert_called_once()
            self.assertEqual(mock_request, payload)


class TestMemoize(unittest.TestCase):
    """Testing for utils.memoize"""

    def test_memoize(self):
        """Testing for utils.memoize"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method") as mock_a:
            mock_a.return_value = True
            test = TestClass()
            test.a_property
            test.a_property
            mock_a.assert_called_once()


if __name__ == '__main__':
    unittest.main()
