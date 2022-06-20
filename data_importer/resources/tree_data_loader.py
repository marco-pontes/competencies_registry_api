import validators
from definitions import BASE_API_URL

IGNORED_PROPERTIES = ['decoded_resource', '@id', '@context']


class TreeDataLoader:
    def __init__(self, resources_manager):
        self.resources_manager = resources_manager
        self.loaded_resources_by_type = {}

    def load_related_resources_tree(self, json_object):
        valid_linked_resources = self.get_valid_linked_resources(json_object)
        resource_type = json_object.get('@type', None)
        uuid = json_object.get('ceterms:ctid', None)
        for key, value in json_object.items():
            if isinstance(value, dict):
                for key, value in value.items():
                    if not key in IGNORED_PROPERTIES:
                        result = dict()
                        result[key] = value
                        self.load_related_resources_tree(result)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        self.load_related_resources_tree(item)
                    elif isinstance(item, str):
                        if key in valid_linked_resources:
                            if not self.resources_manager.is_cached(item):
                                loaded_resource = self.resources_manager.load_resource(item)
                                self.load_related_resources_tree(loaded_resource)
            elif isinstance(value, str):
                if key in valid_linked_resources:
                    if not self.resources_manager.is_cached(value):
                        loaded_resource = self.resources_manager.load_resource(value)
                        self.load_related_resources_tree(loaded_resource)
        type_resource_ids = self.loaded_resources_by_type.get(resource_type, set())
        type_resource_ids.add(uuid)
        self.loaded_resources_by_type[resource_type] = type_resource_ids
        return self.loaded_resources_by_type

    def get_valid_linked_resources(self, json_object):
        linked_resources = set()
        for key, value in json_object.items():
            if key not in IGNORED_PROPERTIES:
                if isinstance(value, str):
                    if validators.url(value) and BASE_API_URL in value:
                        linked_resources.add(key)
                elif isinstance(value, list):
                    item = value[0]
                    if isinstance(item, str) and validators.url(
                            item) and BASE_API_URL in item:
                        linked_resources.add(key)
        return linked_resources
