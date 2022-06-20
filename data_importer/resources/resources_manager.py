from logging import info
from os import path

from data_importer.resources.resource_url import ResourceURL
from definitions import CACHE_DIR


class ResourcesManager:
    def __init__(self, api_client, cache_manager):
        self.api_client = api_client
        self.cache_manager = cache_manager

    def load_all_resources(self):
        file_path = path.join(CACHE_DIR, 'envelopes.json')
        cache_exists = self.cache_manager.cache_exists(file_path)
        if not cache_exists:
            resource_url = ResourceURL(sub_path='envelopes')
            loaded_resource = self.api_client.get(resource_url)
            self.cache_manager.write(file_path, loaded_resource)
        else:
            loaded_resource = self.cache_manager.read(file_path)
        return loaded_resource

    def is_cached(self, url):
        resource_url = ResourceURL(url=url)
        file_path = self.cache_manager.build_file_path(resource_url.uuid, resource_url.sub_path)
        is_cached = self.cache_manager.cache_exists(file_path)
        return is_cached

    def load_resource_by_id(self, uuid, sub_path='resources'):
        resource_url = ResourceURL(sub_path=sub_path, uuid=uuid)
        loaded_resource = self.load_resource(resource_url.complete_url)
        return loaded_resource

    def load_resource(self, url):
        resource_url = ResourceURL(url=url)
        file_path = self.cache_manager.build_file_path(resource_url.uuid, resource_url.sub_path)
        info('Searching for resource {uuid}...'.format(uuid=resource_url.uuid))
        cache_exists = self.cache_manager.cache_exists(file_path)
        if cache_exists:
            loaded_resource = self.cache_manager.read(file_path)
        else:
            loaded_resource = self.api_client.get(resource_url)
            self.cache_manager.write(file_path, loaded_resource)

        return loaded_resource
