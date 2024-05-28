#!/usr/bin/env python3
"""
This module deals with unittests and integration tests

"""
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

git_client = GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests operations in the GithubOrg class"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('git_client.get_json', return_value={"key": "value"})
    def test_org(self, org_object: str, mock_get_json: Mock) -> None:
        """
        Tests that GithubOrgClient.org returns correct value

        """
        git_client = GithubOrgClient(org_object)
        result = git_client.org

        self.assertEqual(result, {"key": "value"})
        mock_get_json.assert_called_once_with(org_object)
    
    def test_public_repos_url(self):
        """
        Tests that this returns the correct URL based on the mocked payload

        """
        payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}
        
        with patch.object(GithubOrgClient, 'org', return_value=payload):
            client = GithubOrgClient("test_org")
            result = client._public_repos_url

            self.assertEqual(result, "https://api.github.com/orgs/test_org/repos")
    
    @patch('utils.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct list of repositories"""
        repo_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = repo_payload

        mock_repos_url = "https://api.github.com/orgs/test_org/repos"
        
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=Mock, return_value=mock_repos_url):
            client = GithubOrgClient("test_org")
            result = client.public_repos()
            
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)
            
            mock_get_json.assert_called_once_with(mock_repos_url)
            self.assertEqual(client._public_repos_url, mock_repos_url)
    
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test that GithubOrgClient.has_license returns the correct boolean value"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos method."""

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to start patcher for requests.get

        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def get_json_side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                return cls.repos_payload
            return {}

        cls.mock_get.return_value.json.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop patcher for requests.get

        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method

        """
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)
        
    def test_public_repos_with_license(self):
        """
        Test the public_repos method with license

        """
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
