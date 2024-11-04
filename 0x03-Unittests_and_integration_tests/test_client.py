#!/usr/bin/env python3
"""Module for working with Client """


from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """ Class for Testing Github Org Client """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """
        Test that GithubOrgClient.org returns the correct value
        for a given organization
        """

        test_class = GithubOrgClient(input)

        # Call the org method, which should call get_json
        test_class.org()

        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')


class TestGithubOrgClient(unittest.TestCase):
    """Class for Testing GithubOrgClient"""

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that _public_repos_url returns the correct repos_url
        based on the mocked org property.
        """
        # Define the payload to mock
        mock_org.return_value = {"repos_url":
                                 "https://api.github.com/orgs/test-org/repos"}

        # Create an instance of GithubOrgClient
        test_client = GithubOrgClient("test-org")

        # Access the _public_repos_url property
        result = test_client._public_repos_url

        self.assertEqual(result, "https://api.github.com/orgs/test-org/repos")


if __name__ == '__main__':
    unittest.main()
