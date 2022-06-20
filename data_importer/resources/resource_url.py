import re
from os import path
from definitions import BASE_API_URL


class ResourceURL:
    def __init__(self, url=None, sub_path=None, uuid=None):
        if url is None and sub_path is None or (url is None and uuid is not None and sub_path is None):
            raise Exception("Url or sub_path are mandatory parameters")
        if url is not None:
            match = re.match(r'https:\/\/staging\.credentialengineregistry\.org\/(\w*)\/?([\w\d-]*)', url)
            if BASE_API_URL not in url or match is None:
                raise Exception("Invalid API URL")
            self.complete_url = url
            if match is not None:
                self.sub_path = match[1]
                self.uuid = match[2]
        else:
            self.complete_url = path.join(BASE_API_URL, sub_path, uuid) if uuid is not None else path.join(BASE_API_URL, sub_path)
            self.uuid = uuid
            self.sub_path = sub_path

    def __str__(self):
        return self.complete_url

