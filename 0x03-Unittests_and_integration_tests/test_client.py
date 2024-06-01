#!/usr/bin/env python3
"""
This module deals with unittests and integration tests

"""
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """
    Includes unit tests for the client.py file

    """
    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json):
        """
        Test that _public_repos_url returns the correct URL

        """
        test_org = 'test_org'
        repos_url = 'https://api.github.com/orgs/test_org/repos'
        mock_get_json.return_value = {"repos_url": repos_url}

        client = GithubOrgClient(test_org)
        result = client._public_repos_url
        self.assertEqual(result, repos_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns the correct list of repositories

        """
        mock_repos_url = 'https://api.github.com/orgs/test_org/repos'
        mock_org = {"repos_url": mock_repos_url}
        mock_repos = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        with patch.object(GithubOrgClient, 'org', new_callable=Mock) as mock_org_method:
            mock_org_method.return_value = mock_org
            mock_get_json.return_value = mock_repos

            client = GithubOrgClient('test_org')
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with(mock_repos_url)

    @patch('client.get_json')
    def test_has_license(self, mock_get_json):
        """
        Test that GithubOrgClient.has_license returns the correct boolean value

        """
        repo = {'license': {'key': 'my_license'}}
        client = GithubOrgClient('test_org')

        result = client.has_license(repo, 'my_license')
        self.assertTrue(result)

        result = client.has_license(repo, 'other_license')
        self.assertFalse(result)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Includes integration tests for the GithubOrgClient class

    """
    @classmethod
    def setUpClass(cls):
        """
        Set up class method

        """
        cls.get_patcher = patch('client.get_json', side_effect=cls.get_json_side_effect)
        cls.mock_get_json = cls.get_patcher.start()
        
        cls.repos_payload = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
            {"name": "repo3", "license": {"key": "apache-2.0"}},
        ]
        cls.org_payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method

        """
        cls.get_patcher.stop()

    @classmethod
    def get_json_side_effect(cls, url):
        """
        Side effect function for get_json

        """
        if url == "https://api.github.com/orgs/test_org":
            return cls.org_payload
        elif url == cls.org_payload["repos_url"]:
            return cls.repos_payload
        return None

    def test_public_repos(self):
        """
        Test public_repos method

        """
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, ["repo1", "repo2", "repo3"])

    def test_public_repos_with_license(self):
        """
        Test the public_repos method with license

        """
        client = GithubOrgClient("test_org")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, ["repo1", "repo3"])


if __name__ == '__main__':
    unittest.main()
