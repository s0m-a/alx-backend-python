#!/usr/bin/env python3
""" Module for testing client """

from fixtures import TEST_PAYLOAD
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """ Class for Testing Github_Org_Client """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, inputs, mock):
        """Test that GithubOrgClient.org returns the correct value."""
        test_class = GithubOrgClient(inputs)
        result = test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{inputs}')
        self.assertEqual(result, mock.return_value)

    def test_public_repos_url(self):
        """
        Verify if the result of _public_repos_url
        corresponds to the expected value based on the mocked payload.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what
        you expect from the chosen payload.
        Test that the mocked property and the mocked
        get_json was called once.
        """
        json_payload = [{"name": "Repo1"}, {"name": "Repo2"},
                        {"name": "Repo3"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for Integration test of fixtures """

    @classmethod
    def setUpClass(cls):
        """A class method called before tests
        in an individual class are run"""
        config = {'return_value.json.side_effect': [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload
            ]
        }

        # Start the patcher using patch as a context manager
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """A class method called after tests
        in an individual class have run"""
        # Stop the patcher
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method
        without specifying a license"""
        # Create an instance of GithubOrgClient
        test_class = GithubOrgClient("google")
        # Check if public_repos returns the expected repositories
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        # Check if public_repos returns an empty list for an invalid license
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        # Check if the mock get method is called
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Test public_repos method with a specified license"""
        # Create an instance of GithubOrgClient
        test_class = GithubOrgClient("google")
        # Check if public_repos returns the expected
        # repositories for Apache-2.0 license
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)
        # Check if public_repos returns the expected
        # repositories for an invalid license
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        # Check if the mock get method is called
        self.mock.assert_called()
