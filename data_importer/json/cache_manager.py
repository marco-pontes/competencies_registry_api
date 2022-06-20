import json
from os.path import exists
from os import fsync, path, makedirs
from logging import info

from definitions import ROOT_DIR, CACHE_DIR


class CacheManager:
    def __init__(self):
        if not path.exists(CACHE_DIR):
            makedirs(CACHE_DIR)
            resources_dir = path.join(CACHE_DIR, 'resources')
            if not path.exists(resources_dir):
                makedirs(resources_dir)
            graph_dir = path.join(CACHE_DIR, 'graph')
            if not path.exists(graph_dir):
                makedirs(graph_dir)

    def read(self, file_path):

        info('Using cached resource: {file_path}'.format(file_path=file_path))
        with open(file_path, 'r') as f:
            file_content = f.read()
            loaded_resource = json.loads(file_content)
        return loaded_resource

    def write(self, file_path, json_data):
        info('Adding resource into cache')
        with open(file_path, 'w') as f:
            f.write(json.dumps(json_data))
            f.flush()
            fsync(f)
            f.close()
        info('Finished writing resource into cache')

    def cache_exists(self, file_path):
        file_exists = exists(file_path)
        return file_exists

    def build_file_path(self, resource_id, sub_path):
        return path.join(CACHE_DIR, sub_path, '{uuid}.json'.format(uuid=resource_id))
