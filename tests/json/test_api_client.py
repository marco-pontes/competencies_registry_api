from unittest.mock import patch, MagicMock

from data_importer.json.api_client import ApiClient
from data_importer.resources.resource_url import ResourceURL


class TestApiClient:
    @patch('requests.Session.get')
    def test_get_returns_json(self, requests_mock):
        mock = MagicMock()
        mock.text = '{"prop1": "test", "prop2": "test2"}'
        requests_mock.return_value = mock
        resource_url = ResourceURL('https://staging.credentialengineregistry.org/envelopes')
        result = ApiClient().get(resource_url)
        expected = {'prop1': 'test', 'prop2': 'test2'}
        assert result == expected


