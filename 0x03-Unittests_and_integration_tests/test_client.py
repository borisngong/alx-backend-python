#!/usr/bin/env python3
""" Module responsible for working with client """

from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Class responsible for Testing GithubOrgClient methods
    """
    lass TestGithubOrgClient(unittest.TestCase):
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
    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that public_repos returns the correct list of repository names
        from the provided JSON payload
        Verifies that both the mocked _public_repos_url property and get_json
        are called exactly once
        """
        # Define mock JSON payload to be returned by get_json
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        # Mock _public_repos_url to prevent actual URL access
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            # Expected list of repository names
            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            # Ensure _public_repos_url and get_json are each called once
            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Unit test for GithubOrgClient.has_license to confirm it
        correctly identifies if a repository has a specified license
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient using fixture data
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up class-level mock for requests.get used in integration tests.
        Patches requests.get with a side effect returning payloads
        for org and repos data based on the configured responses.
        """
        config = {'return_value.json.side_effect': [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """
        Integration test for GithubOrgClient.public_repos with payload
        """
        test_class = GithubOrgClient("google")

        # Check that the org property returns the expected org payload
        self.assertEqual(test_class.org, self.org_payload)

        # Verify that repos_payload matches the expected repos payload
        self.assertEqual(test_class.repos_payload, self.repos_payload)

        # Confirm public_repos returns expected list of repo names
        self.assertEqual(test_class.public_repos(), self.expected_repos)

        # Test with non-matching license should return an empty list
        self.assertEqual(test_class.public_repos("XLICENSE"), [])

        # Ensure the mock was called as expected
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """
        Integration test for public repos with a specific license
        """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)

        self.assertEqual(test_class.public_repos("XLICENSE"), [])

        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)

        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """
        Stops the patcher after all tests in the class have run,
        cleaning up the mock setup for requests.get
        """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
