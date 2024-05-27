#!/usr/bin/env python3
"""
This module deals with unittests and integration tests

"""
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized

git_client = GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests operations in the GithubOrg class"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"key": "value"})
    def test_org(self, org_object: str, mock_get_json: Mock) -> None:
        """
        Tests that GithubOrgClient.org returns correct value

        """
        git_client = GithubOrgClient(org_object)
        result = git_client.org

        self.assertEqual(result, {"key": "value"})
        mock_get_json.assert_called_once_with(org_object)
