from unittest.mock import call, patch
from unittest import TestCase
from os import path
from data_importer.resources.resources_manager import ResourcesManager
from definitions import CACHE_DIR


class TestResourcesManager:
    class TestLoadAllResources(TestCase):
        @patch('data_importer.json.api_client.ApiClient')
        @patch('data_importer.json.cache_manager.CacheManager')
        def test_loads_all_resources_on_the_correct_url(self, api_client_mock, cache_manager_mock):
            api_client_mock.get.return_value = {}
            cache_manager_mock.cache_exists.return_value = False
            resources_manager = ResourcesManager(api_client_mock, cache_manager_mock)
            resources_manager.load_all_resources()
            expected = 'https://staging.credentialengineregistry.org/envelopes'
            assert api_client_mock.get.call_args.args[0].complete_url == expected

        @patch('data_importer.json.api_client.ApiClient')
        @patch('data_importer.json.cache_manager.CacheManager')
        def test_saves_resquested_resource_to_cache(self, api_client_mock, cache_manager_mock):
            api_client_mock.get.return_value = {}
            cache_manager_mock.cache_exists.return_value = False
            resources_manager = ResourcesManager(api_client_mock, cache_manager_mock)
            resources_manager.load_all_resources()
            expected_path = path.join(CACHE_DIR, 'envelopes.json')
            cache_manager_mock.write.assert_called_with(expected_path, {})

        @patch('data_importer.json.api_client.ApiClient')
        @patch('data_importer.json.cache_manager.CacheManager')
        def test_loads_all_resources_from_cache(self, api_client_mock, cache_manager_mock):
            api_client_mock.get.return_value = {}
            cache_manager_mock.cache_exists.return_value = True
            resources_manager = ResourcesManager(api_client_mock, cache_manager_mock)
            resources_manager.load_all_resources()
            expected_path = path.join(CACHE_DIR, 'envelopes.json')
            cache_manager_mock.read.assert_called_with(expected_path)

    class TestIsCached(TestCase):
        @patch('data_importer.json.api_client.ApiClient')
        @patch('data_importer.json.cache_manager.CacheManager')
        def test_is_cached_should_return_true(self, api_client_mock, cache_manager_mock):
            api_client_mock.get.return_value = {}
            cache_manager_mock.cache_exists.return_value = True
            resources_manager = ResourcesManager(api_client_mock, cache_manager_mock)
            result = resources_manager.is_cached('https://staging.credentialengineregistry.org/envelopes')
            assert result is True

        @patch('data_importer.json.api_client.ApiClient')
        @patch('data_importer.json.cache_manager.CacheManager')
        def test_is_cached_should_return_false(self, api_client_mock, cache_manager_mock):
            api_client_mock.get.return_value = {}
            cache_manager_mock.cache_exists.return_value = False
            resources_manager = ResourcesManager(api_client_mock, cache_manager_mock)
            result = resources_manager.is_cached('https://staging.credentialengineregistry.org/envelopes')
            assert result is False



    class TestLoadResourceById(TestCase):
        @patch('data_importer.json.api_client.ApiClient')
        @patch('data_importer.json.cache_manager.CacheManager')
        def test_should_return_correct_object(self, api_client_mock, cache_manager_mock):
            api_client_mock.get.return_value = {'loadedProp': 'test'}
            cache_manager_mock.cache_exists.return_value = False
            resources_manager = ResourcesManager(api_client_mock, cache_manager_mock)
            result = resources_manager.load_resource_by_id(uuid='12ea-99bc-44fc')
            assert result == {'loadedProp': 'test'}

        @patch('data_importer.json.api_client.ApiClient')
        @patch('data_importer.json.cache_manager.CacheManager')
        def test_should_call_the_correct_api_url(self, api_client_mock, cache_manager_mock):
            api_client_mock.get.return_value = {'loadedProp': 'test'}
            cache_manager_mock.cache_exists.return_value = False
            resources_manager = ResourcesManager(api_client_mock, cache_manager_mock)
            resources_manager.load_resource_by_id(uuid='12ea-99bc-44fc')
            expected = 'https://staging.credentialengineregistry.org/resources/12ea-99bc-44fc'
            assert api_client_mock.get.call_args.args[0].complete_url == expected

        @patch('data_importer.json.api_client.ApiClient')
        @patch('data_importer.json.cache_manager.CacheManager')
        def test_should_write_to_cache(self, api_client_mock, cache_manager_mock):
            api_client_mock.get.return_value = {'loadedProp': 'test'}
            cache_manager_mock.cache_exists.return_value = False
            cache_manager_mock.build_file_path.return_value = 'path/to/file.json'
            resources_manager = ResourcesManager(api_client_mock, cache_manager_mock)
            resources_manager.load_resource_by_id(uuid='12ea-99bc-44fc')
            cache_manager_mock.write.assert_called_with('path/to/file.json', {'loadedProp': 'test'})

        @patch('data_importer.json.api_client.ApiClient')
        @patch('data_importer.json.cache_manager.CacheManager')
        def test_should_return_correct_cached_object(self, api_client_mock, cache_manager_mock):
            api_client_mock.get.return_value = {'loadedProp': 'test'}
            cache_manager_mock.cache_exists.return_value = True
            cache_manager_mock.read.return_value = {'readObject': 'test from cache'}
            resources_manager = ResourcesManager(api_client_mock, cache_manager_mock)
            result = resources_manager.load_resource_by_id(uuid='12ea-99bc-44fc')
            assert result == {'readObject': 'test from cache'}

        @patch('data_importer.json.api_client.ApiClient')
        @patch('data_importer.json.cache_manager.CacheManager')
        def test_should_not_call_api_client(self, api_client_mock, cache_manager_mock):
            api_client_mock.get.return_value = {'loadedProp': 'test'}
            cache_manager_mock.cache_exists.return_value = True
            resources_manager = ResourcesManager(api_client_mock, cache_manager_mock)
            resources_manager.load_resource_by_id(uuid='12ea-99bc-44fc')
            api_client_mock.get.assert_not_called()

        @patch('data_importer.json.api_client.ApiClient')
        @patch('data_importer.json.cache_manager.CacheManager')
        def test_should_load_from_the_correct_cache_path(self, api_client_mock, cache_manager_mock):
            api_client_mock.get.return_value = {'loadedProp': 'test'}
            cache_manager_mock.cache_exists.return_value = True
            cache_manager_mock.build_file_path.return_value = 'path/to/file.json'
            resources_manager = ResourcesManager(api_client_mock, cache_manager_mock)
            resources_manager.load_resource_by_id(uuid='12ea-99bc-44fc')
            cache_manager_mock.read.assert_called_with('path/to/file.json')
