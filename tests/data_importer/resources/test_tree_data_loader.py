from unittest.mock import call, patch

from data_importer.resources.tree_data_loader import TreeDataLoader


class TestTreeDataLoader:

    @patch('data_importer.resources.resources_manager.ResourcesManager')
    def test_loads_no_contained_resource(self, resources_manager_mock):
        resources_manager_mock.is_cached.return_value = False
        resources_manager_mock.load_resource.return_value = {'prop1': 'related resource'}
        tree_data_loader = TreeDataLoader(resources_manager_mock)
        json_object = {'prop1': 'https://teste.com', 'prop2': 'Test', 'prop3': ''}
        tree_data_loader.load_related_resources_tree(json_object)
        resources_manager_mock.load_resource.assert_not_called()

    @patch('data_importer.resources.resources_manager.ResourcesManager')
    def test_loads_contained_resource(self, resources_manager_mock):
        resources_manager_mock.is_cached.return_value = False
        resources_manager_mock.load_resource.return_value = {'prop1': 'related resource'}
        tree_data_loader = TreeDataLoader(resources_manager_mock)
        json_object = {'prop1': 'https://staging.credentialengineregistry.org/resources/a1cd-334f-55ab', 'prop2': 'Test', 'prop3': ''}
        tree_data_loader.load_related_resources_tree(json_object)
        resources_manager_mock.load_resource.assert_called_with('https://staging.credentialengineregistry.org/resources/a1cd-334f-55ab')

    @patch('data_importer.resources.resources_manager.ResourcesManager')
    def test_loads_nested_contained_resource(self, resources_manager_mock):
        resources_manager_mock.is_cached.return_value = False
        resources_manager_mock.is_cached.side_effect = [False, False, True]
        resources_manager_mock.load_resource.return_value = {'prop1': 'related resource', 'prop2': 'https://staging.credentialengineregistry.org/resources/c4f7d-554f-88ac'}
        tree_data_loader = TreeDataLoader(resources_manager_mock)
        json_object = {'prop1': 'https://staging.credentialengineregistry.org/resources/a1cd-334f-55ab', 'prop2': 'Test', 'prop3': ''}
        tree_data_loader.load_related_resources_tree(json_object)
        resources_manager_mock.load_resource.assert_has_calls([call('https://staging.credentialengineregistry.org/resources/a1cd-334f-55ab'),
                                                                   call('https://staging.credentialengineregistry.org/resources/c4f7d-554f-88ac')])