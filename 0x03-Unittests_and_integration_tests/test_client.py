#!/usr/bin/env python3
"""
This module deals with unittests and integration tests

"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from requests import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """
    Includes unit tests for the client.py file

    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json", return_value={"key": "value"})
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """
        Tests that org returns correct value

        """
        git_client = GithubOrgClient(org_name)
        result = git_client.org
        self.assertEqual(result, {"key": "value"})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

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
        Test that public_repos returns the correct list of repos

        """
        repo_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = repo_payload
        mock_repos_url = 'https://api.github.com/orgs/test_org/repos'

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = mock_repos_url
            client = GithubOrgClient('test_org')
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with(mock_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license returns the correct boolean value

        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Includes integration tests for the GithubOrgClient class

    """
    @classmethod
    def setUpClass(cls):
        """
        Set up class method

        """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

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
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test the public_repos method with license

        """
        client = GithubOrgClient("test_org")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
